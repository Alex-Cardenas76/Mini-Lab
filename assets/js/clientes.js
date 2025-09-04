document.addEventListener('DOMContentLoaded', function() {
    try {
        // Control del nuevo menú móvil de barra superior
        const menuToggle = document.getElementById('pd-menu-toggle');
        const topbarMenu = document.getElementById('pd-topbar-menu');
        const menuClose = document.getElementById('pd-menu-close');

        if (menuToggle && topbarMenu && menuClose) {
            menuToggle.addEventListener('click', function() {
                topbarMenu.classList.add('active');
            });

            menuClose.addEventListener('click', function() {
                topbarMenu.classList.remove('active');
            });
        } else {
            console.error('No se encontraron los elementos del nuevo menú móvil');
        }
    } catch (error) {
        console.error('Error al inicializar el nuevo menú móvil:', error);
    }

// Mostrar modal de nuevo cliente
document.getElementById('btnNuevoCliente').addEventListener('click', function() {
    limpiarYMostrarModal('nuevo');
});

document.getElementById('cerrarModal').addEventListener('click', function() {
    document.getElementById('nuevoClienteModal').style.display = 'none';
    document.getElementById('modalBackdrop').style.display = 'none';
});

document.getElementById('cancelarCliente').addEventListener('click', function() {
    document.getElementById('nuevoClienteModal').style.display = 'none';
    document.getElementById('modalBackdrop').style.display = 'none';
});

// Lógica de filtrado de clientes
function aplicarFiltrosClientes() {
    const filtroNombre = document.getElementById('filtroNombre').value.toLowerCase();
    const filtroTipo = document.getElementById('filtroTipo').value;
    const filas = document.querySelectorAll('.table tbody tr');

    filas.forEach(fila => {
        const nombre = fila.children[1].textContent.toLowerCase();
        const tipo = fila.children[2].textContent.toLowerCase();
        let mostrar = true;

        if (filtroNombre && !nombre.includes(filtroNombre)) {
            mostrar = false;
        }
        if (filtroTipo && tipo !== filtroTipo) {
            mostrar = false;
        }
        fila.style.display = mostrar ? '' : 'none';
    });
}
// Asignar evento al botón de aplicar filtros
const btnAplicarFiltros = document.querySelector('.card.mb-3 .btn.btn-primary');
if (btnAplicarFiltros) {
    btnAplicarFiltros.addEventListener('click', aplicarFiltrosClientes);
}

// --- NUEVO: Lógica para guardar cliente y agregarlo a la tabla ---
document.getElementById('guardarCliente').addEventListener('click', function() {
    const nombre = document.getElementById('nombre').value.trim();
    const tipo = document.getElementById('tipoCliente').value;
    const contacto = document.getElementById('contacto').value.trim();
    const nombreIE = document.getElementById('nombreIE').value.trim();
    const direccion = document.getElementById('direccion').value.trim();
    const detalles = document.getElementById('detallesAdicionales').value.trim();

    // Validación básica
    if (!nombre || !contacto || !direccion) {
        alert('Por favor, complete los campos obligatorios: Nombre, Contacto y Dirección.');
        return;
    }

    // Generar un ID simple
    const filas = document.querySelectorAll('.table tbody tr');
    const id = 'C' + (filas.length + 1).toString().padStart(3, '0');

    // Crear la fila
    const tr = document.createElement('tr');
    tr.innerHTML = `
        <td data-label="ID">${id}</td>
        <td data-label="Nombre">${nombre}</td>
        <td data-label="Tipo">${tipo === 'institucion' ? 'Colegio' : 'Particular'}</td>
        <td data-label="Contacto">${contacto}</td>
        <td data-label="Nombre I.E">${tipo === 'institucion' ? nombreIE : '-'}</td>
        <td data-label="Dirección">${direccion}</td>
        <td data-label="Detalles Adicionales">${detalles || '-'}</td>
        <td class="actions">
            <button class="btn btn-sm btn-ver">Ver</button>
            <button class="btn btn-sm btn-editar">Editar</button>
            <button class="btn btn-sm btn-eliminar">Eliminar</button>
        </td>
    `;
    document.querySelector('.table tbody').appendChild(tr);

    // Limpiar formulario y cerrar modal
    document.getElementById('formNuevoCliente').reset();
    document.getElementById('nuevoClienteModal').style.display = 'none';
    document.getElementById('modalBackdrop').style.display = 'none';

    // Volver a asignar eventos a los nuevos botones
    asignarEventosVerEditar();
    asignarEventoEliminar();
});

// --- NUEVO: Función para limpiar y mostrar el modal en modo adecuado ---
function limpiarYMostrarModal(modo, datos = {}) {
    const form = document.getElementById('formNuevoCliente');
    form.reset();
    // Rellenar datos si es ver o editar
    if (modo !== 'nuevo' && datos) {
        document.getElementById('nombre').value = datos.nombre || '';
        document.getElementById('tipoCliente').value = datos.tipoCliente || 'particular';
        document.getElementById('contacto').value = datos.contacto || '';
        document.getElementById('nombreIE').value = datos.nombreIE || '';
        document.getElementById('direccion').value = datos.direccion || '';
        document.getElementById('detallesAdicionales').value = datos.detalles || '';
    }
    // Habilitar/deshabilitar campos y mostrar/ocultar botón guardar
    const campos = form.querySelectorAll('input, select, textarea');
    if (modo === 'ver') {
        campos.forEach(c => c.disabled = true);
        document.getElementById('guardarCliente').style.display = 'none';
    } else {
        campos.forEach(c => c.disabled = false);
        document.getElementById('guardarCliente').style.display = 'inline-block';
    }
    document.getElementById('nuevoClienteModal').style.display = 'block';
    document.getElementById('modalBackdrop').style.display = 'block';
}

// --- NUEVO: Asignar eventos a los botones Ver y Editar ---
function asignarEventosVerEditar() {
    document.querySelectorAll('.btn-ver').forEach(btn => {
        btn.onclick = function() {
            const fila = btn.closest('tr');
            const datos = {
                nombre: fila.children[1].textContent,
                tipoCliente: fila.children[2].textContent.toLowerCase() === 'colegio' ? 'institucion' : 'particular',
                contacto: fila.children[3].textContent,
                nombreIE: fila.children[4].textContent !== '-' ? fila.children[4].textContent : '',
                direccion: fila.children[5].textContent,
                detalles: fila.children[6].textContent !== '-' ? fila.children[6].textContent : ''
            };
            limpiarYMostrarModal('ver', datos);
        }
    });
    document.querySelectorAll('.btn-editar').forEach(btn => {
        btn.onclick = function() {
            const fila = btn.closest('tr');
            const datos = {
                nombre: fila.children[1].textContent,
                tipoCliente: fila.children[2].textContent.toLowerCase() === 'colegio' ? 'institucion' : 'particular',
                contacto: fila.children[3].textContent,
                nombreIE: fila.children[4].textContent !== '-' ? fila.children[4].textContent : '',
                direccion: fila.children[5].textContent,
                detalles: fila.children[6].textContent !== '-' ? fila.children[6].textContent : ''
            };
            limpiarYMostrarModal('editar', datos);
            // Al guardar, actualizar la fila (esto se puede mejorar para edición real)
            document.getElementById('guardarCliente').onclick = function() {
                // Validación básica
                const nombre = document.getElementById('nombre').value.trim();
                const tipo = document.getElementById('tipoCliente').value;
                const contacto = document.getElementById('contacto').value.trim();
                const nombreIE = document.getElementById('nombreIE').value.trim();
                const direccion = document.getElementById('direccion').value.trim();
                const detalles = document.getElementById('detallesAdicionales').value.trim();
                if (!nombre || !contacto || !direccion) {
                    alert('Por favor, complete los campos obligatorios: Nombre, Contacto y Dirección.');
                    return;
                }
                fila.children[1].textContent = nombre;
                fila.children[2].textContent = tipo === 'institucion' ? 'Colegio' : 'Particular';
                fila.children[3].textContent = contacto;
                fila.children[4].textContent = tipo === 'institucion' ? nombreIE : '-';
                fila.children[5].textContent = direccion;
                fila.children[6].textContent = detalles || '-';
                document.getElementById('nuevoClienteModal').style.display = 'none';
                document.getElementById('modalBackdrop').style.display = 'none';
            }
        }
    });
}

// --- NUEVO: Asignar evento a los botones Eliminar ---
function asignarEventoEliminar() {
    document.querySelectorAll('.btn-eliminar').forEach(btn => {
        btn.onclick = function() {
            const fila = btn.closest('tr');
            if (confirm('¿Estás seguro de que deseas eliminar este cliente?')) {
                fila.remove();
            }
        }
    });
}

// Asignar eventos al cargar la página
asignarEventosVerEditar();
asignarEventoEliminar();

});