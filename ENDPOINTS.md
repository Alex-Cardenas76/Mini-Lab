# Endpoints del Sistema de Gestión Empresarial Multi-tenant

## 🔐 Autenticación y Usuarios (`usuarios/`)

### Autenticación
- `POST /api/auth/login/` - Iniciar sesión
- `POST /api/auth/logout/` - Cerrar sesión
- `POST /api/auth/register/` - Registro de usuario
- `POST /api/auth/verify-code/` - Verificar código de seguridad
- `POST /api/auth/reset-password/` - Restablecer contraseña

### Gestión de Usuarios
- `GET /api/usuarios/` - Listar usuarios del tenant
- `POST /api/usuarios/` - Crear usuario
- `GET /api/usuarios/{id}/` - Obtener usuario
- `PUT /api/usuarios/{id}/` - Actualizar usuario
- `DELETE /api/usuarios/{id}/` - Eliminar usuario
- `GET /api/usuarios/groups/` - Listar grupos
- `POST /api/usuarios/{id}/assign-group/` - Asignar grupo

## 🏢 Gestión de Tenants (`tenants/`)

- `GET /api/tenants/` - Listar tenants
- `POST /api/tenants/` - Crear tenant
- `GET /api/tenants/{id}/` - Obtener tenant
- `PUT /api/tenants/{id}/` - Actualizar tenant
- `DELETE /api/tenants/{id}/` - Eliminar tenant
- `PUT /api/tenants/{id}/status/` - Cambiar estado (active/inactive/suspended)

## 👥 Gestión de Clientes (`clientes/`)

- `GET /api/clientes/` - Listar clientes del tenant
- `POST /api/clientes/` - Crear cliente
- `GET /api/clientes/{id}/` - Obtener cliente
- `PUT /api/clientes/{id}/` - Actualizar cliente
- `DELETE /api/clientes/{id}/` - Eliminar cliente
- `GET /api/clientes/search/?q={query}` - Buscar clientes

## 📋 Gestión de Pedidos (`pedidos/`)

### Pedidos
- `GET /api/pedidos/` - Listar pedidos del tenant
- `POST /api/pedidos/` - Crear pedido
- `GET /api/pedidos/{id}/` - Obtener pedido
- `PUT /api/pedidos/{id}/` - Actualizar pedido
- `DELETE /api/pedidos/{id}/` - Eliminar pedido
- `PUT /api/pedidos/{id}/status/` - Cambiar estado del pedido

### Detalles de Pedido
- `GET /api/pedidos/{id}/detalles/` - Listar detalles del pedido
- `POST /api/pedidos/{id}/detalles/` - Agregar detalle al pedido
- `PUT /api/pedidos/{pedido_id}/detalles/{id}/` - Actualizar detalle
- `DELETE /api/pedidos/{pedido_id}/detalles/{id}/` - Eliminar detalle

## 📄 Gestión de Contratos (`contratos/`)

- `GET /api/contratos/` - Listar contratos del tenant
- `POST /api/contratos/` - Crear contrato
- `GET /api/contratos/{id}/` - Obtener contrato
- `PUT /api/contratos/{id}/` - Actualizar contrato
- `DELETE /api/contratos/{id}/` - Eliminar contrato
- `PUT /api/contratos/{id}/status/` - Cambiar estado del contrato

## 🏭 Gestión de Producción (`produccion/`)

### Órdenes de Producción
- `GET /api/produccion/ordenes/` - Listar órdenes del tenant
- `POST /api/produccion/ordenes/` - Crear orden de producción
- `GET /api/produccion/ordenes/{id}/` - Obtener orden
- `PUT /api/produccion/ordenes/{id}/` - Actualizar orden
- `PUT /api/produccion/ordenes/{id}/status/` - Cambiar estado

### Varillas
- `GET /api/produccion/varillas/` - Listar varillas del tenant
- `POST /api/produccion/varillas/` - Crear varilla
- `GET /api/produccion/varillas/{id}/` - Obtener varilla
- `PUT /api/produccion/varillas/{id}/` - Actualizar varilla
- `DELETE /api/produccion/varillas/{id}/` - Eliminar varilla

### Cuadros
- `GET /api/produccion/cuadros/` - Listar cuadros
- `POST /api/produccion/cuadros/` - Crear cuadro
- `GET /api/produccion/cuadros/{id}/` - Obtener cuadro
- `PUT /api/produccion/cuadros/{id}/` - Actualizar cuadro
- `PUT /api/produccion/cuadros/{id}/status/` - Cambiar estado

### Movimientos de Inventario
- `GET /api/produccion/movimientos/` - Listar movimientos
- `POST /api/produccion/movimientos/` - Registrar movimiento
- `GET /api/produccion/movimientos/{id}/` - Obtener movimiento

## 📦 Gestión de Materiales (`materiales/`)

### Pintura y Acabados
- `GET /api/materiales/pintura-acabado/` - Listar pinturas
- `POST /api/materiales/pintura-acabado/` - Crear pintura
- `GET /api/materiales/pintura-acabado/{id}/` - Obtener pintura
- `PUT /api/materiales/pintura-acabado/{id}/` - Actualizar pintura

### Materiales de Impresión
- `GET /api/materiales/impresion/` - Listar materiales
- `POST /api/materiales/impresion/` - Crear material
- `GET /api/materiales/impresion/{id}/` - Obtener material
- `PUT /api/materiales/impresion/{id}/` - Actualizar material

### Materiales Recordatorio
- `GET /api/materiales/recordatorio/` - Listar materiales
- `POST /api/materiales/recordatorio/` - Crear material
- `GET /api/materiales/recordatorio/{id}/` - Obtener material
- `PUT /api/materiales/recordatorio/{id}/` - Actualizar material

### Software y Equipos
- `GET /api/materiales/software-equipo/` - Listar software/equipos
- `POST /api/materiales/software-equipo/` - Crear software/equipo
- `GET /api/materiales/software-equipo/{id}/` - Obtener software/equipo
- `PUT /api/materiales/software-equipo/{id}/` - Actualizar software/equipo

### Materiales de Pintura
- `GET /api/materiales/material-pintura/` - Listar materiales
- `POST /api/materiales/material-pintura/` - Crear material
- `GET /api/materiales/material-pintura/{id}/` - Obtener material
- `PUT /api/materiales/material-pintura/{id}/` - Actualizar material

### Materiales de Diseño
- `GET /api/materiales/material-diseno/` - Listar materiales
- `POST /api/materiales/material-diseno/` - Crear material
- `GET /api/materiales/material-diseno/{id}/` - Obtener material
- `PUT /api/materiales/material-diseno/{id}/` - Actualizar material

### Productos Terminados
- `GET /api/materiales/productos-terminados/` - Listar productos
- `POST /api/materiales/productos-terminados/` - Crear producto
- `GET /api/materiales/productos-terminados/{id}/` - Obtener producto
- `PUT /api/materiales/productos-terminados/{id}/` - Actualizar producto
- `PUT /api/materiales/productos-terminados/{id}/status/` - Cambiar estado

## 📊 Gestión de Inventario (`inventario/`)

- `GET /api/inventario/` - Listar inventario del tenant
- `GET /api/inventario/{item_type}/` - Listar por tipo de item
- `GET /api/inventario/{item_type}/{item_id}/` - Obtener item específico
- `PUT /api/inventario/{item_type}/{item_id}/stock/` - Actualizar stock
- `GET /api/inventario/alerts/` - Alertas de stock mínimo
- `GET /api/inventario/report/` - Reporte de inventario

## 📅 Gestión de Agenda (`agenda/`)

- `GET /api/agenda/` - Listar eventos del tenant
- `POST /api/agenda/` - Crear evento
- `GET /api/agenda/{id}/` - Obtener evento
- `PUT /api/agenda/{id}/` - Actualizar evento
- `DELETE /api/agenda/{id}/` - Eliminar evento
- `PUT /api/agenda/{id}/status/` - Cambiar estado del evento
- `GET /api/agenda/calendar/?date={date}` - Eventos por fecha

## 🔧 Endpoints de Utilidad

### Búsqueda Global
- `GET /api/search/?q={query}&type={type}` - Búsqueda global

### Reportes
- `GET /api/reports/ventas/?start_date={date}&end_date={date}` - Reporte de ventas
- `GET /api/reports/produccion/?start_date={date}&end_date={date}` - Reporte de producción
- `GET /api/reports/inventario/` - Reporte de inventario

### Configuración
- `GET /api/config/document-types/` - Tipos de documentos
- `GET /api/config/permissions/` - Permisos disponibles

## 📝 Notas Importantes

- **Multi-tenant**: Todos los endpoints están aislados por `tenant_id`
- **Autenticación**: Requiere token de autenticación en headers
- **Filtros**: Usar query parameters para filtros (ej: `?status=active`)
- **Paginación**: Usar `?page={number}&page_size={size}`
- **Estados**: Cada entidad tiene estados específicos (pendiente, en_proceso, completado, etc.)

- Si falta desarrollar algun otro endpoint tendra que desarrollarlo y comunicarlo a su Scrum Master.
