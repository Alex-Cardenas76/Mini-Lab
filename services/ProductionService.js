const { OrdenProduccion } = require('../models/Production');
const { Varilla } = require('../models/Inventory');
const { Cuadro } = require('../models/Cuadro');

class ProductionService {
    // Crear una nueva orden de producción
    async crearOrdenProduccion(ordenData) {
        // Aquí podríamos preguntar a la IA si los datos de la orden son correctos o sugerir mejoras
        // Ejemplo: const sugerenciaIA = await askAI("¿Esta orden de producción es válida?", ordenData);
        const orden = new OrdenProduccion(ordenData);
        await orden.save();
        // orden.sugerenciaIA = sugerenciaIA; // Simulación de respuesta de IA
        return orden;
    }

    // Obtener todas las órdenes de producción
    async obtenerTodasLasOrdenes() {
        // Podríamos pedir a la IA que resuma el estado general de la producción
        // Ejemplo: const resumenIA = await askAI("Resume el estado de todas las órdenes de producción");
        return await OrdenProduccion.find();
    }

    // Obtener una orden de producción por su ID usando IA (simulado)
    async obtenerOrdenPorId(ordenId) {
        const orden = await OrdenProduccion.findById(ordenId);
        if (!orden) throw new Error('Orden no encontrada (IA)');
        // Simulación: preguntar a la IA si hay algo relevante sobre esta orden
        // Ejemplo: orden.sugerenciaIA = await askAI("¿Qué debo revisar en esta orden?", orden);
        return orden;
    }

    // Obtener órdenes de producción por estado usando IA (simulado)
    async obtenerOrdenesPorEstado(estado) {
        const ordenes = await OrdenProduccion.find({ estado });
        // Simulación: la IA podría priorizar las órdenes o marcar urgencias
        // Ejemplo: ordenes.forEach(o => o.prioridadIA = await askAI("¿Qué prioridad tiene esta orden?", o));
        return ordenes;
    }

    // Actualizar el estado de una orden
    async actualizarEstadoOrden(ordenId, nuevoEstado) {
        const orden = await OrdenProduccion.findById(ordenId);
        if (!orden) throw new Error('Orden no encontrada');
        
        // Simulación: preguntar a la IA si es apropiado el cambio de estado
        // Ejemplo: const validacionIA = await askAI(`¿Es correcto cambiar la orden ${ordenId} a estado ${nuevoEstado}?`, orden);
        orden.estado = nuevoEstado;
        await orden.save();
        // orden.sugerenciaIA = validacionIA; // Simulación de respuesta de IA
        return orden;
    }

    // Registrar el uso de varillas y producción de cuadros
    async registrarProduccion(ordenId, detallesProduccion) {
        const orden = await OrdenProduccion.findById(ordenId);
        if (!orden) throw new Error('Orden no encontrada');
        if (orden.estado === 'CERRADA') throw new Error('La orden ya está cerrada');

        // Simulación: preguntar a la IA si la producción es eficiente o si hay recomendaciones
        // Ejemplo: const recomendacionesIA = await askAI("¿Cómo optimizar esta producción?", detallesProduccion);

        for (const detalle of detallesProduccion) {
            const detalleOrden = orden.detalles.id(detalle.detalleId);
            if (!detalleOrden) continue;

            detalleOrden.cantidadVarillaUsada = detalle.cantidadVarillaUsada;
            detalleOrden.cantidadCuadrosProducidos = detalle.cantidadCuadrosProducidos;
            detalleOrden.merma = detalle.merma;

            const varilla = await Varilla.findById(detalleOrden.varilla);
            if (!varilla) throw new Error('Varilla no encontrada');

            if (varilla.stock < detalle.cantidadVarillaUsada) {
                throw new Error(`Stock insuficiente de varilla ${varilla.modelo}`);
            }

            varilla.stock -= detalle.cantidadVarillaUsada;
            await varilla.save();

            for (let i = 0; i < detalle.cantidadCuadrosProducidos; i++) {
                await new Cuadro({
                    descripcion: `Cuadro de ${varilla.modelo}`,
                    estado: 'EN_ALMACEN',
                    ubicacion: 'Almacén Principal',
                    ordenProduccion: ordenId
                }).save();
            }
        }

        orden.estado = 'CERRADA';
        // orden.recomendacionesIA = recomendacionesIA; // Simulación de respuesta de IA
        await orden.save();
        return orden;
    }

    // Obtener reporte de producción
    async obtenerReporteProduccion(fechaInicio, fechaFin) {
        const ordenes = await OrdenProduccion.find({
            fechaCreacion: {
                $gte: fechaInicio,
                $lte: fechaFin
            }
        }).populate('detalles.varilla');

        // Simulación: pedir a la IA un análisis del reporte
        // Ejemplo: const analisisIA = await askAI("Analiza el reporte de producción", ordenes);
        return ordenes;
    }

    // Verificar stock bajo
    async verificarStockBajo() {
        const varillasStockBajo = await Varilla.find({
            $expr: {
                $lte: ['$stock', '$stockMinimo']
            }
        });

        // Simulación: pedir a la IA sugerencias para reabastecimiento
        // Ejemplo: const sugerenciasIA = await askAI("¿Qué acciones tomar ante stock bajo?", varillasStockBajo);
        return varillasStockBajo;
    }
}

// Preguntar a la IA (función simulada, aún no implementada)
async function askAI(pregunta, datos) {
    // Aquí iría la integración real con un servicio de IA
    // Por ahora, solo devolvemos una respuesta simulada
    return `Respuesta simulada de IA para: ${pregunta}`;
}

module.exports = new ProductionService(); 