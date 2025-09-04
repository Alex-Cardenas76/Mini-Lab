// Mostrar el botón solo en móvil
if (window.innerWidth <= 768) {
    document.getElementById('menuToggle').style.display = 'block';
}
window.addEventListener('resize', function() {
    if (window.innerWidth <= 768) {
        document.getElementById('menuToggle').style.display = 'block';
    } else {
        document.getElementById('menuToggle').style.display = 'none';
    }
});

// Control del menú móvil (idéntico a clientes.html)
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.querySelector('.sidebar');
menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('active');
    menuToggle.classList.toggle('menu-active');
});

// Cerrar menú al hacer clic fuera (solo móvil)
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && !sidebar.contains(e.target) && !menuToggle.contains(e.target) && sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
        menuToggle.classList.remove('menu-active');
    }
});

function mostrarDetalle(id, cliente, servicio, estado, fecha, total) {
    document.getElementById('detalleId').textContent = id;
    document.getElementById('detalleCliente').textContent = cliente;
    document.getElementById('detalleServicio').textContent = servicio;
    document.getElementById('detalleEstado').textContent = estado;
    document.getElementById('detalleFecha').textContent = fecha;
    document.getElementById('detalleTotal').textContent = total;
    document.getElementById('detallePedidoModal').style.display = 'block';
    document.getElementById('detalleBackdrop').style.display = 'block';
}
function cerrarDetalle() {
    document.getElementById('detallePedidoModal').style.display = 'none';
    document.getElementById('detalleBackdrop').style.display = 'none';
}

// Funciones para verificar stock y calcular tiempos
function verificarStockPapel() {
    const tipoPapel = document.getElementById('tipoPapel').value;
    const stockInfo = document.getElementById('stockPapel');
    
    // Simular verificación de stock
    const stock = obtenerStockPapel(tipoPapel);
    if (stock < 10) {
        stockInfo.innerHTML = `<span class="text-danger">Stock bajo: ${stock} unidades</span>`;
    } else {
        stockInfo.innerHTML = `<span class="text-success">Stock disponible: ${stock} unidades</span>`;
    }
}

function verificarStockMarco() {
    const tipoMarco = document.getElementById('tipoMarco').value;
    const stockInfo = document.getElementById('stockMarco');
    
    // Simular verificación de stock
    const stock = obtenerStockMarco(tipoMarco);
    if (stock < 5) {
        stockInfo.innerHTML = `<span class="text-danger">Stock bajo: ${stock} unidades</span>`;
    } else {
        stockInfo.innerHTML = `<span class="text-success">Stock disponible: ${stock} unidades</span>`;
    }
}

function verificarStockRecordatorio() {
    const plantilla = document.getElementById('plantillaRecordatorio').value;
    const stockInfo = document.getElementById('stockRecordatorio');
    
    // Simular verificación de stock
    const stock = obtenerStockRecordatorio(plantilla);
    if (stock < 20) {
        stockInfo.innerHTML = `<span class="text-danger">Stock bajo: ${stock} unidades</span>`;
    } else {
        stockInfo.innerHTML = `<span class="text-success">Stock disponible: ${stock} unidades</span>`;
    }
}

function calcularTiempoEstimado() {
    const tipoServicio = document.getElementById('tipoServicio').value;
    let tiempoEstimado = '';
    
    switch(tipoServicio) {
        case 'impresion':
            const cantidadFotos = document.getElementById('cantidadFotos').value;
            tiempoEstimado = `${Math.ceil(cantidadFotos / 50)} horas`;
            break;
        case 'enmarcado':
            const ancho = document.getElementById('anchoMarco').value;
            const alto = document.getElementById('altoMarco').value;
            tiempoEstimado = `${Math.ceil((ancho * alto) / 100)} horas`;
            break;
        case 'recordatorio':
            const cantidad = document.getElementById('cantidadRecordatorios').value;
            tiempoEstimado = `${Math.ceil(cantidad / 100)} días`;
            break;
        case 'retoque':
            const tipoRetoque = document.getElementById('tipoRetoque').value;
            tiempoEstimado = tipoRetoque === 'restauracion' ? '2-3 días' : '1 día';
            break;
    }
    
    document.getElementById('tiempoEstimado').value = tiempoEstimado;
}

function verificarCapacidadProduccion() {
    const fechaEntrega = document.getElementById('fechaEntrega').value;
    const tipoServicio = document.getElementById('tipoServicio').value;
    
    // Simular verificación de capacidad
    const capacidad = obtenerCapacidadProduccion(fechaEntrega, tipoServicio);
    if (!capacidad) {
        alert('No hay capacidad de producción disponible para la fecha seleccionada');
        document.getElementById('fechaEntrega').value = '';
    }
}

// Funciones simuladas para obtener datos
function obtenerStockPapel(tipo) {
    // Simular consulta a base de datos
    return Math.floor(Math.random() * 50);
}

function obtenerStockMarco(tipo) {
    // Simular consulta a base de datos
    return Math.floor(Math.random() * 20);
}

function obtenerStockRecordatorio(plantilla) {
    // Simular consulta a base de datos
    return Math.floor(Math.random() * 100);
}

function obtenerCapacidadProduccion(fecha, tipo) {
    // Simular consulta a base de datos
    return Math.random() > 0.3; // 70% de probabilidad de tener capacidad
}

// Función para crear nuevo pedido
async function crearNuevoPedido(datos) {
    try {
        // 1. Verificar stock disponible
        const stockDisponible = await verificarStock(datos.materiales);
        if (!stockDisponible) {
            alert('No hay suficiente stock para procesar este pedido');
            return;
        }

        // 2. Crear el pedido
        const pedido = await guardarPedido(datos);
        
        // 3. Generar orden de producción automáticamente
        const ordenProduccion = await crearOrdenProduccion({
            pedidoId: pedido.id,
            tipoServicio: datos.tipoServicio,
            materiales: datos.materiales,
            fechaInicio: new Date(),
            fechaFinEstimada: datos.fechaEntrega,
            estado: 'pendiente',
            prioridad: datos.prioridad
        });
        
        // 4. Actualizar inventario
        await actualizarInventario(pedido.materiales);
        
        // 5. Actualizar la interfaz
        actualizarTablaPedidos();
        cerrarModal();
        
        // 6. Mostrar confirmación con detalles
        alert(`Pedido creado exitosamente\nID: ${pedido.id}\nOrden de Producción: ${ordenProduccion.id}`);
    } catch (error) {
        console.error('Error al crear pedido:', error);
        alert('Error al crear el pedido');
    }
}

// Función para verificar stock
async function verificarStock(materiales) {
    // Simular inventario disponible (aquí irían tus datos reales)
    const inventarioSimulado = {
        'papel': 150, // unidades de papel
        'marco': 10,  // unidades de marcos
        'plantilla': 80 // unidades de plantillas
        // Agrega otros materiales aquí
    };

    let stockSuficiente = true;

    for (const material of materiales) {
        const tipoMaterial = material.tipo;
        const cantidadRequerida = parseInt(material.cantidad, 10); // Asegúrate de que sea un número

        // Verificar si el material existe en el inventario simulado
        if (!inventarioSimulado.hasOwnProperty(tipoMaterial)) {
            console.warn(`Material desconocido en inventario simulado: ${tipoMaterial}`);
            // Puedes decidir si esto detiene el pedido o no. Por ahora, asumimos que sí.
            stockSuficiente = false;
            alert(`Falta información de stock para el material: ${tipoMaterial}`);
            break; // Detener la verificación si un material es desconocido o falta stock
        }

        const stockActual = inventarioSimulado[tipoMaterial];

        if (stockActual < cantidadRequerida) {
            stockSuficiente = false;
            alert(`Stock insuficiente para ${tipoMaterial}. Requerido: ${cantidadRequerida}, Disponible: ${stockActual}`);
            break; // Detener la verificación si no hay stock
        }
    }

    return stockSuficiente; // Devuelve true si hay stock para todo, false si no
}

// Función para guardar pedido
async function guardarPedido(datos) {
    // Simular guardado de pedido
    return {
        id: 'P' + Math.floor(Math.random() * 1000),
        ...datos
    };
}

// Función mejorada para crear orden de producción
async function crearOrdenProduccion(datos) {
    try {
        // Simular creación de orden de producción
        const orden = {
            id: 'PR' + Math.floor(Math.random() * 1000),
            ...datos,
            fechaCreacion: new Date(),
            progreso: 0
        };
        
        // Notificar a la página de producción
        window.dispatchEvent(new CustomEvent('nuevaOrdenProduccion', { 
            detail: orden 
        }));
        
        return orden;
    } catch (error) {
        console.error('Error al crear orden de producción:', error);
        throw error;
    }
}

// Función para actualizar inventario
async function actualizarInventario(materiales) {
    // Simular actualización de inventario
    console.log('Actualizando inventario con:', materiales);
}

// Función para actualizar la tabla de pedidos
async function actualizarTablaPedidos() {
    try {
        // Obtener todos los pedidos (simulación)
        const pedidos = await obtenerPedidos();
        
        // Obtener el tbody de la tabla
        const tbody = document.querySelector('.table tbody');
        if (!tbody) return;

        // Limpiar la tabla
        tbody.innerHTML = '';

        // Agregar cada pedido a la tabla
        pedidos.forEach(pedido => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${pedido.id}</td>
                <td>${pedido.cliente}</td>
                <td>${pedido.tipoServicio}</td>
                <td><span class="badge badge-${pedido.estado === 'nuevo' ? 'info' : pedido.estado === 'produccion' ? 'warning' : 'success'}">${pedido.estado}</span></td>
                <td>${pedido.fotografias || '-'}</td>
                <td>${pedido.diseño || '-'}</td>
                <td>${pedido.materiales || '-'}</td>
                <td class="actions">
                    <button class="btn btn-sm btn-ver" onclick="mostrarDetalle('${pedido.id}', '${pedido.cliente}', '${pedido.tipoServicio}', '${pedido.estado}', '${pedido.fecha}', '${pedido.total}')">Ver</button>
                    <button class="btn btn-sm btn-editar" onclick="editarPedido('${pedido.id}')">Editar</button>
                </td>
            `;
            tbody.appendChild(tr);
        });

        // Actualizar la paginación
        actualizarPaginacion(pedidos.length);
    } catch (error) {
        console.error('Error al actualizar la tabla de pedidos:', error);
    }
}

// Función simulada para obtener pedidos
async function obtenerPedidos() {
    // Simulación de datos - aquí iría la consulta real a la base de datos
    return [
        {
            id: 'P006',
            cliente: 'Nuevo Cliente',
            tipoServicio: 'Impresión Minilab',
            estado: 'nuevo',
            fecha: new Date().toLocaleDateString(),
            total: 'S/ 50.00',
            fotografias: '10 fotos',
            diseño: '-',
            materiales: 'Papel fotográfico'
        }
    ];
}

// Función para actualizar la paginación
function actualizarPaginacion(totalPedidos) {
    const paginacion = document.querySelector('.pagination');
    if (!paginacion) return;

    // Simulación de paginación - aquí iría la lógica real
    const paginaActual = 1;
    const totalPaginas = Math.ceil(totalPedidos / 10);

    paginacion.innerHTML = `
        <button class="btn btn-anterior" onclick="cambiarPagina(${paginaActual - 1})">Anterior</button>
        <span>Página ${paginaActual} de ${totalPaginas}</span>
        <button class="btn btn-siguiente" onclick="cambiarPagina(${paginaActual + 1})">Siguiente</button>
    `;
}

// Función para cambiar de página
function cambiarPagina(pagina) {
    // Aquí iría la lógica para cambiar de página
    console.log('Cambiar a página:', pagina);
}

// Función para cerrar el modal de nuevo pedido
function cerrarModalNuevoPedido() {
    const modal = document.getElementById('nuevoPedidoModal');
    const backdrop = document.getElementById('modalBackdrop');
    
    if (modal && backdrop) {
        modal.style.display = 'none';
        backdrop.style.display = 'none';
        
        // Limpiar el formulario
        const form = document.getElementById('formNuevoPedido');
        if (form) {
            form.reset();
        }
        
        // Ocultar campos de servicio
        document.querySelectorAll('.campos-servicio').forEach(element => {
            element.style.display = 'none';
        });
        // Restaurar el texto del botón
        const guardarBtn = document.getElementById('guardarPedido');
        if (guardarBtn) guardarBtn.textContent = 'Guardar Pedido';
        idPedidoEditando = null;
    }
}

// Configurar eventos del modal
function configurarEventosModal() {
    // Event listener para el botón de nuevo pedido
    const btnNuevoPedido = document.getElementById('btnNuevoPedido');
    if (btnNuevoPedido) {
        btnNuevoPedido.addEventListener('click', () => {
            const modal = document.getElementById('nuevoPedidoModal');
            const backdrop = document.getElementById('modalBackdrop');
            if (modal && backdrop) {
                modal.style.display = 'block';
                backdrop.style.display = 'block';
            }
        });
    }

    // Cerrar modal al hacer clic en el botón de cerrar
    const cerrarModalBtn = document.getElementById('cerrarModal');
    if (cerrarModalBtn) {
        cerrarModalBtn.addEventListener('click', cerrarModalNuevoPedido);
    }

    // Cerrar modal al hacer clic en el botón de cancelar
    const cancelarPedidoBtn = document.getElementById('cancelarPedido');
    if (cancelarPedidoBtn) {
        cancelarPedidoBtn.addEventListener('click', cerrarModalNuevoPedido);
    }

    // Cerrar modal al hacer clic fuera del modal
    const backdrop = document.getElementById('modalBackdrop');
    if (backdrop) {
        backdrop.addEventListener('click', (e) => {
            if (e.target === backdrop) {
                cerrarModalNuevoPedido();
            }
        });
    }

    // Mostrar campos dinámicos según el tipo de servicio
    const tipoServicioSelect = document.getElementById('tipoServicio');
    if (tipoServicioSelect) {
        tipoServicioSelect.addEventListener('change', (e) => {
            // Ocultar todos los campos de servicio
            document.querySelectorAll('#camposServicio > div').forEach(element => element.style.display = 'none');
            // Mostrar campos correspondientes al servicio seleccionado
            const camposServicio = document.querySelector(`.campos-${e.target.value}`);
            if (camposServicio) {
                camposServicio.style.display = 'block';
            }
        });
    }

    // Guardar pedido
    const guardarPedidoBtn = document.getElementById('guardarPedido');
    if (guardarPedidoBtn) {
        guardarPedidoBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            // Obtener datos del formulario
            const datosPedido = {
                tipoCliente: document.getElementById('tipoCliente').value,
                cliente: document.getElementById('cliente').options[document.getElementById('cliente').selectedIndex].text,
                tipoServicio: document.getElementById('tipoServicio').value,
                fechaEntrega: document.getElementById('fechaEntrega').value,
                prioridad: document.getElementById('prioridad').value,
                estado: 'nuevo',
                materiales: []
            };
            // Validar campos requeridos
            if (!datosPedido.cliente || !datosPedido.tipoServicio || !datosPedido.fechaEntrega) {
                alert('Por favor, complete todos los campos requeridos');
                return;
            }
            // Agregar materiales según el tipo de servicio
            switch (datosPedido.tipoServicio) {
                case 'impresion':
                    datosPedido.materiales.push({
                        tipo: 'papel',
                        cantidad: document.getElementById('cantidadFotos').value
                    });
                    break;
                case 'enmarcado':
                    datosPedido.materiales.push({
                        tipo: 'marco',
                        cantidad: '1'
                    });
                    break;
                case 'recordatorio':
                    datosPedido.materiales.push({
                        tipo: 'plantilla',
                        cantidad: document.getElementById('cantidadRecordatorios').value
                    });
                    break;
                case 'retoque':
                    datosPedido.materiales.push({
                        tipo: 'retoque',
                        cantidad: '1'
                    });
                    break;
            }
            // Verificar stock disponible
            if (!await verificarStock(datosPedido.materiales)) {
                return;
            }
            if (idPedidoEditando) {
                // Actualizar la fila en la tabla
                const filas = document.querySelectorAll('.table tbody tr');
                filas.forEach(fila => {
                    if (fila.children[0].textContent === idPedidoEditando) {
                        fila.children[1].textContent = datosPedido.cliente;
                        fila.children[2].textContent = datosPedido.tipoServicio.charAt(0).toUpperCase() + datosPedido.tipoServicio.slice(1);
                        // Puedes actualizar más columnas si lo deseas
                    }
                });
                idPedidoEditando = null;
                guardarPedidoBtn.textContent = 'Guardar Pedido';
                cerrarModalNuevoPedido();
                return;
            }
            // Crear el pedido
            await crearNuevoPedido(datosPedido);
            // Actualizar la tabla de pedidos
            actualizarTablaPedidos();
            // Cerrar el modal
            cerrarModalNuevoPedido();
        });
    }
}

// Inicializar eventos del modal cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', configurarEventosModal);

// Lógica de filtrado de pedidos
function aplicarFiltrosPedidos() {
    const filtroCliente = document.getElementById('filtroCliente').value.toLowerCase();
    const filtroServicio = document.getElementById('filtroServicio').value.toLowerCase();
    const filtroEstado = document.getElementById('filtroEstado').value.toLowerCase();
    const filas = document.querySelectorAll('.table tbody tr');

    filas.forEach(fila => {
        const cliente = fila.children[1].textContent.toLowerCase();
        const servicio = fila.children[2].textContent.toLowerCase();
        // El estado puede estar dentro de un span
        let estado = '';
        const estadoSpan = fila.children[3].querySelector('span');
        if (estadoSpan) {
            estado = estadoSpan.textContent.toLowerCase();
        } else {
            estado = fila.children[3].textContent.toLowerCase();
        }
        let mostrar = true;

        if (filtroCliente && !cliente.includes(filtroCliente)) {
            mostrar = false;
        }
        if (filtroServicio && !servicio.includes(filtroServicio)) {
            mostrar = false;
        }
        if (filtroEstado && !estado.includes(filtroEstado)) {
            mostrar = false;
        }
        fila.style.display = mostrar ? '' : 'none';
    });
}

// Asignar evento al botón de aplicar filtros
const btnAplicarFiltros = document.querySelector('.form-group.text-right .btn.btn-primary');
if (btnAplicarFiltros) {
    btnAplicarFiltros.addEventListener('click', (e) => {
        e.preventDefault();
        aplicarFiltrosPedidos();
    });
}

// Función para editar pedido
let idPedidoEditando = null;
function editarPedido(id) {
    // Buscar la fila del pedido por ID
    const filas = document.querySelectorAll('.table tbody tr');
    let datos = null;
    filas.forEach(fila => {
        if (fila.children[0].textContent === id) {
            datos = {
                id: fila.children[0].textContent,
                cliente: fila.children[1].textContent,
                tipoServicio: fila.children[2].textContent,
                estado: fila.children[3].textContent,
                // Puedes agregar más campos si los tienes en la tabla
            };
        }
    });
    if (!datos) return;
    // Llenar el formulario del modal
    document.getElementById('tipoCliente').value = 'particular'; // Por defecto, puedes mejorar esto
    // Seleccionar el cliente en el select
    const clienteSelect = document.getElementById('cliente');
    for (let i = 0; i < clienteSelect.options.length; i++) {
        if (clienteSelect.options[i].text === datos.cliente) {
            clienteSelect.selectedIndex = i;
            break;
        }
    }
    // Seleccionar el tipo de servicio
    document.getElementById('tipoServicio').value = datos.tipoServicio.toLowerCase().replace(' ', '');
    // Mostrar campos dinámicos
    const event = new Event('change');
    document.getElementById('tipoServicio').dispatchEvent(event);
    // Puedes llenar más campos aquí si lo deseas
    // Mostrar el modal
    document.getElementById('nuevoPedidoModal').style.display = 'block';
    document.getElementById('modalBackdrop').style.display = 'block';
    // Cambiar el texto del botón a 'Actualizar Pedido'
    const guardarBtn = document.getElementById('guardarPedido');
    guardarBtn.textContent = 'Actualizar Pedido';
    idPedidoEditando = id;
}