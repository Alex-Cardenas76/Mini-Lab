const { 
    Varilla, 
    PinturaAcabado, 
    MaterialImpresion, 
    MaterialRecordatorio, 
    SoftwareEquipo, 
    MaterialPintura, 
    MaterialDiseno, 
    ProductoTerminado 
} = require('../models/Inventory');
const { OrdenProduccion } = require('../models/Production');

class InventoryService {
    // ===== SERVICIOS PRINCIPALES =====

    // 1.1 Enmarcado de Fotografías - Varillas/Molduras
    async obtenerVarillas() {
        return await Varilla.find().sort({ nombre: 1 });
    }

    async crearVarilla(varillaData) {
        const varilla = new Varilla(varillaData);
        await varilla.save();
        return varilla;
    }

    async actualizarVarilla(id, varillaData) {
        return await Varilla.findByIdAndUpdate(id, varillaData, { new: true });
    }

    async eliminarVarilla(id) {
        return await Varilla.findByIdAndDelete(id);
    }

    // 1.1 Enmarcado de Fotografías - Pinturas y Acabados
    async obtenerPinturasAcabados() {
        return await PinturaAcabado.find().sort({ producto: 1 });
    }

    async crearPinturaAcabado(pinturaData) {
        const pintura = new PinturaAcabado(pinturaData);
        await pintura.save();
        return pintura;
    }

    async actualizarPinturaAcabado(id, pinturaData) {
        return await PinturaAcabado.findByIdAndUpdate(id, pinturaData, { new: true });
    }

    async eliminarPinturaAcabado(id) {
        return await PinturaAcabado.findByIdAndDelete(id);
    }

    // 1.2 Impresión de Fotografías - Materiales de Impresión
    async obtenerMaterialesImpresion() {
        return await MaterialImpresion.find().sort({ producto: 1 });
    }

    async crearMaterialImpresion(materialData) {
        const material = new MaterialImpresion(materialData);
        await material.save();
        return material;
    }

    async actualizarMaterialImpresion(id, materialData) {
        return await MaterialImpresion.findByIdAndUpdate(id, materialData, { new: true });
    }

    async eliminarMaterialImpresion(id) {
        return await MaterialImpresion.findByIdAndDelete(id);
    }

    // 1.3 Recordatorios Escolares - Materiales
    async obtenerMaterialesRecordatorio() {
        return await MaterialRecordatorio.find().sort({ producto: 1 });
    }

    async crearMaterialRecordatorio(materialData) {
        const material = new MaterialRecordatorio(materialData);
        await material.save();
        return material;
    }

    async actualizarMaterialRecordatorio(id, materialData) {
        return await MaterialRecordatorio.findByIdAndUpdate(id, materialData, { new: true });
    }

    async eliminarMaterialRecordatorio(id) {
        return await MaterialRecordatorio.findByIdAndDelete(id);
    }

    // ===== SERVICIOS ARTÍSTICOS =====

    // 2.1 Restauración Digital - Software y Equipos
    async obtenerSoftwareEquipos() {
        return await SoftwareEquipo.find().sort({ producto: 1 });
    }

    async crearSoftwareEquipo(softwareData) {
        const software = new SoftwareEquipo(softwareData);
        await software.save();
        return software;
    }

    async actualizarSoftwareEquipo(id, softwareData) {
        return await SoftwareEquipo.findByIdAndUpdate(id, softwareData, { new: true });
    }

    async eliminarSoftwareEquipo(id) {
        return await SoftwareEquipo.findByIdAndDelete(id);
    }

    // 2.2 Pintura al Óleo - Materiales
    async obtenerMaterialesPintura() {
        return await MaterialPintura.find().sort({ producto: 1 });
    }

    async crearMaterialPintura(materialData) {
        const material = new MaterialPintura(materialData);
        await material.save();
        return material;
    }

    async actualizarMaterialPintura(id, materialData) {
        return await MaterialPintura.findByIdAndUpdate(id, materialData, { new: true });
    }

    async eliminarMaterialPintura(id) {
        return await MaterialPintura.findByIdAndDelete(id);
    }

    // 2.3 Edición Gráfica - Materiales de Diseño
    async obtenerMaterialesDiseno() {
        return await MaterialDiseno.find().sort({ producto: 1 });
    }

    async crearMaterialDiseno(materialData) {
        const material = new MaterialDiseno(materialData);
        await material.save();
        return material;
    }

    async actualizarMaterialDiseno(id, materialData) {
        return await MaterialDiseno.findByIdAndUpdate(id, materialData, { new: true });
    }

    async eliminarMaterialDiseno(id) {
        return await MaterialDiseno.findByIdAndDelete(id);
    }

    // ===== PRODUCTOS TERMINADOS =====
    async obtenerProductosTerminados() {
        return await ProductoTerminado.find().sort({ fechaCreacion: -1 });
    }

    async crearProductoTerminado(productoData) {
        const producto = new ProductoTerminado(productoData);
        await producto.save();
        return producto;
    }

    async actualizarProductoTerminado(id, productoData) {
        return await ProductoTerminado.findByIdAndUpdate(id, productoData, { new: true });
    }

    async eliminarProductoTerminado(id) {
        return await ProductoTerminado.findByIdAndDelete(id);
    }

    // ===== FUNCIONES GENERALES =====

    // Obtener alertas de stock bajo para todos los tipos de materiales
    async obtenerAlertasStockBajo() {
        const alertas = [];

        // Verificar varillas
        const varillasStockBajo = await Varilla.find({
            $expr: { $lte: ['$stockActual', '$stockMinimo'] }
        });
        alertas.push(...varillasStockBajo.map(v => ({
            tipo: 'Varilla',
            producto: v.nombre,
            stockActual: v.stockActual,
            stockMinimo: v.stockMinimo
        })));

        // Verificar pinturas y acabados
        const pinturasStockBajo = await PinturaAcabado.find({
            $expr: { $lte: ['$stockActual', '$stockMinimo'] }
        });
        alertas.push(...pinturasStockBajo.map(p => ({
            tipo: 'Pintura/Acabado',
            producto: p.producto,
            stockActual: p.stockActual,
            stockMinimo: p.stockMinimo
        })));

        // Verificar materiales de impresión
        const materialesImpresionStockBajo = await MaterialImpresion.find({
            $expr: { $lte: ['$stockActual', '$stockMinimo'] }
        });
        alertas.push(...materialesImpresionStockBajo.map(m => ({
            tipo: 'Material Impresión',
            producto: m.producto,
            stockActual: m.stockActual,
            stockMinimo: m.stockMinimo
        })));

        // Verificar materiales de recordatorio
        const materialesRecordatorioStockBajo = await MaterialRecordatorio.find({
            $expr: { $lte: ['$stockActual', '$stockMinimo'] }
        });
        alertas.push(...materialesRecordatorioStockBajo.map(m => ({
            tipo: 'Material Recordatorio',
            producto: m.producto,
            stockActual: m.stockActual,
            stockMinimo: m.stockMinimo
        })));

        // Verificar software y equipos
        const softwareStockBajo = await SoftwareEquipo.find({
            $expr: { $lte: ['$stockActual', '$stockMinimo'] }
        });
        alertas.push(...softwareStockBajo.map(s => ({
            tipo: 'Software/Equipo',
            producto: s.producto,
            stockActual: s.stockActual,
            stockMinimo: s.stockMinimo
        })));

        // Verificar materiales de pintura
        const materialesPinturaStockBajo = await MaterialPintura.find({
            $expr: { $lte: ['$stockActual', '$stockMinimo'] }
        });
        alertas.push(...materialesPinturaStockBajo.map(m => ({
            tipo: 'Material Pintura',
            producto: m.producto,
            stockActual: m.stockActual,
            stockMinimo: m.stockMinimo
        })));

        // Verificar materiales de diseño
        const materialesDisenoStockBajo = await MaterialDiseno.find({
            $expr: { $lte: ['$stockActual', '$stockMinimo'] }
        });
        alertas.push(...materialesDisenoStockBajo.map(m => ({
            tipo: 'Material Diseño',
            producto: m.producto,
            stockActual: m.stockActual,
            stockMinimo: m.stockMinimo
        })));

        return alertas;
    }

    // Obtener resumen general del inventario
    async obtenerResumenInventario() {
        const [
            varillas,
            pinturas,
            materialesImpresion,
            materialesRecordatorio,
            software,
            materialesPintura,
            materialesDiseno,
            productosTerminados
        ] = await Promise.all([
            Varilla.countDocuments(),
            PinturaAcabado.countDocuments(),
            MaterialImpresion.countDocuments(),
            MaterialRecordatorio.countDocuments(),
            SoftwareEquipo.countDocuments(),
            MaterialPintura.countDocuments(),
            MaterialDiseno.countDocuments(),
            ProductoTerminado.countDocuments()
        ]);

        return {
            totalVarillas: varillas,
            totalPinturas: pinturas,
            totalMaterialesImpresion: materialesImpresion,
            totalMaterialesRecordatorio: materialesRecordatorio,
            totalSoftware: software,
            totalMaterialesPintura: materialesPintura,
            totalMaterialesDiseno: materialesDiseno,
            totalProductosTerminados: productosTerminados
        };
    }

    // Registrar entrada de varillas
    async registrarEntrada(varillaId, cantidad, motivo) {
        const varilla = await Varilla.findById(varillaId);
        if (!varilla) throw new Error('Varilla no encontrada');

        varilla.stock += cantidad;
        await varilla.save();

        // Registrar el movimiento en el historial
        await this.registrarMovimiento(varillaId, 'ENTRADA', cantidad, motivo);
        
        return varilla;
    }

    // Registrar salida de varillas
    async registrarSalida(varillaId, cantidad, motivo) {
        const varilla = await Varilla.findById(varillaId);
        if (!varilla) throw new Error('Varilla no encontrada');

        if (varilla.stock < cantidad) {
            throw new Error(`Stock insuficiente. Disponible: ${varilla.stock}`);
        }

        varilla.stock -= cantidad;
        await varilla.save();

        // Registrar el movimiento en el historial
        await this.registrarMovimiento(varillaId, 'SALIDA', cantidad, motivo);
        
        return varilla;
    }

    // Verificar stock disponible
    async verificarStock(varillaId, cantidadNecesaria) {
        const varilla = await Varilla.findById(varillaId);
        if (!varilla) throw new Error('Varilla no encontrada');

        return {
            disponible: varilla.stock,
            suficiente: varilla.stock >= cantidadNecesaria,
            faltante: Math.max(0, cantidadNecesaria - varilla.stock)
        };
    }

    // Obtener historial de movimientos
    async obtenerHistorialMovimientos(varillaId, fechaInicio, fechaFin) {
        return await MovimientoInventario.find({
            varilla: varillaId,
            fecha: {
                $gte: fechaInicio,
                $lte: fechaFin
            }
        }).sort({ fecha: -1 });
    }

    // Obtener alertas de stock
    async obtenerAlertasStock() {
        const varillasStockBajo = await Varilla.find({
            $expr: {
                $lte: ['$stock', '$stockMinimo']
            }
        });

        return varillasStockBajo.map(varilla => ({
            modelo: varilla.modelo,
            stockActual: varilla.stock,
            stockMinimo: varilla.stockMinimo,
            faltante: varilla.stockMinimo - varilla.stock
        }));
    }
}

module.exports = new InventoryService(); 