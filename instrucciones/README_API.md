# Equipo de APIs - Instrucciones de Desarrollo

## Responsabilidad Principal
Construir la capa de APIs usando Django REST Framework para exponer los datos del sistema.

## Alcance de Trabajo

### ✅ Tareas Incluidas
- Crear serializers para todos los modelos
- Implementar ViewSets y APIViews
- Definir rutas API con prefijo /api/v1/
- Implementar CRUD básico para cada entidad
- Configurar filtrado por tenant_id
- Implementar paginación y filtros

### ❌ Tareas Excluidas
- Modificar vistas existentes (responsabilidad del equipo de vistas)
- Configurar autenticación (responsabilidad del equipo de autenticación)
- Modificar configuración global (responsabilidad del equipo de configuración)
- Modificar modelos existentes

## Estructura de APIs Requerida

### Prefijo Base
Todas las rutas deben usar el prefijo: `/api/v1/`

### Autenticación
- Implementar autenticación por tokens
- Headers requeridos: `Authorization: Token {token}`
- Verificar tenant_id en cada request

### Respuestas Estándar
- Formato JSON consistente
- Códigos de estado HTTP apropiados
- Mensajes de error descriptivos
- Paginación en listas

## Módulos a Desarrollar

### 1. Autenticación y Usuarios
**Archivo**: `usuarios/serializers.py`, `usuarios/api_views.py`

#### Endpoints de Autenticación
- `POST /api/v1/auth/login/` - Iniciar sesión
- `POST /api/v1/auth/logout/` - Cerrar sesión
- `POST /api/v1/auth/register/` - Registro de usuario
- `POST /api/v1/auth/verify-code/` - Verificar código de seguridad
- `POST /api/v1/auth/reset-password/` - Restablecer contraseña

#### Endpoints de Usuarios
- `GET /api/v1/usuarios/` - Listar usuarios del tenant
- `POST /api/v1/usuarios/` - Crear usuario
- `GET /api/v1/usuarios/{id}/` - Obtener usuario
- `PUT /api/v1/usuarios/{id}/` - Actualizar usuario
- `DELETE /api/v1/usuarios/{id}/` - Eliminar usuario
- `GET /api/v1/usuarios/groups/` - Listar grupos
- `POST /api/v1/usuarios/{id}/assign-group/` - Asignar grupo

### 2. Gestión de Tenants
**Archivo**: `tenants/serializers.py`, `tenants/api_views.py`

#### Endpoints
- `GET /api/v1/tenants/` - Listar tenants
- `POST /api/v1/tenants/` - Crear tenant
- `GET /api/v1/tenants/{id}/` - Obtener tenant
- `PUT /api/v1/tenants/{id}/` - Actualizar tenant
- `DELETE /api/v1/tenants/{id}/` - Eliminar tenant
- `PUT /api/v1/tenants/{id}/status/` - Cambiar estado

### 3. Gestión de Clientes
**Archivo**: `clientes/serializers.py`, `clientes/api_views.py`

#### Endpoints
- `GET /api/v1/clientes/` - Listar clientes del tenant
- `POST /api/v1/clientes/` - Crear cliente
- `GET /api/v1/clientes/{id}/` - Obtener cliente
- `PUT /api/v1/clientes/{id}/` - Actualizar cliente
- `DELETE /api/v1/clientes/{id}/` - Eliminar cliente
- `GET /api/v1/clientes/search/?q={query}` - Buscar clientes

### 4. Gestión de Pedidos
**Archivo**: `pedidos/serializers.py`, `pedidos/api_views.py`

#### Endpoints de Pedidos
- `GET /api/v1/pedidos/` - Listar pedidos del tenant
- `POST /api/v1/pedidos/` - Crear pedido
- `GET /api/v1/pedidos/{id}/` - Obtener pedido
- `PUT /api/v1/pedidos/{id}/` - Actualizar pedido
- `DELETE /api/v1/pedidos/{id}/` - Eliminar pedido
- `PUT /api/v1/pedidos/{id}/status/` - Cambiar estado

#### Endpoints de Detalles
- `GET /api/v1/pedidos/{id}/detalles/` - Listar detalles
- `POST /api/v1/pedidos/{id}/detalles/` - Agregar detalle
- `PUT /api/v1/pedidos/{pedido_id}/detalles/{id}/` - Actualizar detalle
- `DELETE /api/v1/pedidos/{pedido_id}/detalles/{id}/` - Eliminar detalle

### 5. Gestión de Contratos
**Archivo**: `contratos/serializers.py`, `contratos/api_views.py`

#### Endpoints
- `GET /api/v1/contratos/` - Listar contratos del tenant
- `POST /api/v1/contratos/` - Crear contrato
- `GET /api/v1/contratos/{id}/` - Obtener contrato
- `PUT /api/v1/contratos/{id}/` - Actualizar contrato
- `DELETE /api/v1/contratos/{id}/` - Eliminar contrato
- `PUT /api/v1/contratos/{id}/status/` - Cambiar estado

### 6. Gestión de Producción
**Archivo**: `produccion/serializers.py`, `produccion/api_views.py`

#### Endpoints de Órdenes
- `GET /api/v1/produccion/ordenes/` - Listar órdenes
- `POST /api/v1/produccion/ordenes/` - Crear orden
- `GET /api/v1/produccion/ordenes/{id}/` - Obtener orden
- `PUT /api/v1/produccion/ordenes/{id}/` - Actualizar orden
- `PUT /api/v1/produccion/ordenes/{id}/status/` - Cambiar estado

#### Endpoints de Varillas
- `GET /api/v1/produccion/varillas/` - Listar varillas
- `POST /api/v1/produccion/varillas/` - Crear varilla
- `GET /api/v1/produccion/varillas/{id}/` - Obtener varilla
- `PUT /api/v1/produccion/varillas/{id}/` - Actualizar varilla
- `DELETE /api/v1/produccion/varillas/{id}/` - Eliminar varilla

#### Endpoints de Cuadros
- `GET /api/v1/produccion/cuadros/` - Listar cuadros
- `POST /api/v1/produccion/cuadros/` - Crear cuadro
- `GET /api/v1/produccion/cuadros/{id}/` - Obtener cuadro
- `PUT /api/v1/produccion/cuadros/{id}/` - Actualizar cuadro
- `PUT /api/v1/produccion/cuadros/{id}/status/` - Cambiar estado

#### Endpoints de Movimientos
- `GET /api/v1/produccion/movimientos/` - Listar movimientos
- `POST /api/v1/produccion/movimientos/` - Registrar movimiento
- `GET /api/v1/produccion/movimientos/{id}/` - Obtener movimiento

### 7. Gestión de Materiales
**Archivo**: `materiales/serializers.py`, `materiales/api_views.py`

#### Endpoints por Tipo de Material
- `GET /api/v1/materiales/pintura-acabado/` - Listar pinturas
- `POST /api/v1/materiales/pintura-acabado/` - Crear pintura
- `GET /api/v1/materiales/pintura-acabado/{id}/` - Obtener pintura
- `PUT /api/v1/materiales/pintura-acabado/{id}/` - Actualizar pintura

- `GET /api/v1/materiales/impresion/` - Listar materiales impresión
- `POST /api/v1/materiales/impresion/` - Crear material impresión
- `GET /api/v1/materiales/impresion/{id}/` - Obtener material impresión
- `PUT /api/v1/materiales/impresion/{id}/` - Actualizar material impresión

- `GET /api/v1/materiales/recordatorio/` - Listar materiales recordatorio
- `POST /api/v1/materiales/recordatorio/` - Crear material recordatorio
- `GET /api/v1/materiales/recordatorio/{id}/` - Obtener material recordatorio
- `PUT /api/v1/materiales/recordatorio/{id}/` - Actualizar material recordatorio

- `GET /api/v1/materiales/software-equipo/` - Listar software/equipos
- `POST /api/v1/materiales/software-equipo/` - Crear software/equipo
- `GET /api/v1/materiales/software-equipo/{id}/` - Obtener software/equipo
- `PUT /api/v1/materiales/software-equipo/{id}/` - Actualizar software/equipo

- `GET /api/v1/materiales/material-pintura/` - Listar materiales pintura
- `POST /api/v1/materiales/material-pintura/` - Crear material pintura
- `GET /api/v1/materiales/material-pintura/{id}/` - Obtener material pintura
- `PUT /api/v1/materiales/material-pintura/{id}/` - Actualizar material pintura

- `GET /api/v1/materiales/material-diseno/` - Listar materiales diseño
- `POST /api/v1/materiales/material-diseno/` - Crear material diseño
- `GET /api/v1/materiales/material-diseno/{id}/` - Obtener material diseño
- `PUT /api/v1/materiales/material-diseno/{id}/` - Actualizar material diseño

- `GET /api/v1/materiales/productos-terminados/` - Listar productos terminados
- `POST /api/v1/materiales/productos-terminados/` - Crear producto terminado
- `GET /api/v1/materiales/productos-terminados/{id}/` - Obtener producto terminado
- `PUT /api/v1/materiales/productos-terminados/{id}/` - Actualizar producto terminado
- `PUT /api/v1/materiales/productos-terminados/{id}/status/` - Cambiar estado

### 8. Gestión de Inventario
**Archivo**: `inventario/serializers.py`, `inventario/api_views.py`

#### Endpoints
- `GET /api/v1/inventario/` - Listar inventario del tenant
- `GET /api/v1/inventario/{item_type}/` - Listar por tipo de item
- `GET /api/v1/inventario/{item_type}/{item_id}/` - Obtener item específico
- `PUT /api/v1/inventario/{item_type}/{item_id}/stock/` - Actualizar stock
- `GET /api/v1/inventario/alerts/` - Alertas de stock mínimo
- `GET /api/v1/inventario/report/` - Reporte de inventario

### 9. Gestión de Agenda
**Archivo**: `agenda/serializers.py`, `agenda/api_views.py`

#### Endpoints
- `GET /api/v1/agenda/` - Listar eventos del tenant
- `POST /api/v1/agenda/` - Crear evento
- `GET /api/v1/agenda/{id}/` - Obtener evento
- `PUT /api/v1/agenda/{id}/` - Actualizar evento
- `DELETE /api/v1/agenda/{id}/` - Eliminar evento
- `PUT /api/v1/agenda/{id}/status/` - Cambiar estado del evento
- `GET /api/v1/agenda/calendar/?date={date}` - Eventos por fecha

## Endpoints de Utilidad

### Búsqueda Global
**Archivo**: `config/api_views.py`
- `GET /api/v1/search/?q={query}&type={type}` - Búsqueda global

### Reportes
**Archivo**: `config/api_views.py`
- `GET /api/v1/reports/ventas/?start_date={date}&end_date={date}` - Reporte de ventas
- `GET /api/v1/reports/produccion/?start_date={date}&end_date={date}` - Reporte de producción
- `GET /api/v1/reports/inventario/` - Reporte de inventario

### Configuración
**Archivo**: `config/api_views.py`
- `GET /api/v1/config/document-types/` - Tipos de documentos
- `GET /api/v1/config/permissions/` - Permisos disponibles

## Estructura de Archivos Requerida

### Serializers
Para cada app, crear archivo `serializers.py`:
- Serializer para cada modelo
- Serializers anidados para relaciones
- Validación de datos
- Campos calculados si es necesario

### API Views
Para cada app, crear archivo `api_views.py`:
- ViewSets para CRUD completo
- APIViews para endpoints específicos
- Filtros y búsquedas
- Paginación

### URLs de API
Para cada app, crear archivo `api_urls.py`:
- Rutas para todos los endpoints
- Agrupación por funcionalidad
- Parámetros de URL

## Consideraciones Técnicas

### Filtrado por Tenant
- Implementar filtro automático por tenant_id
- Verificar tenant en cada operación
- No exponer datos de otros tenants

### Paginación
- Implementar paginación estándar
- Límite de elementos por página
- Información de paginación en respuesta

### Filtros y Búsquedas
- Filtros por campos comunes
- Búsqueda por texto
- Filtros por fechas
- Filtros por estado

### Validación
- Validación de datos de entrada
- Mensajes de error descriptivos
- Validación de relaciones
- Validación de permisos

### Respuestas HTTP
- Códigos de estado apropiados
- Formato JSON consistente
- Mensajes de error claros
- Información de paginación

## Entregables Esperados

### Archivos de Serializers
- `usuarios/serializers.py`
- `tenants/serializers.py`
- `clientes/serializers.py`
- `pedidos/serializers.py`
- `contratos/serializers.py`
- `produccion/serializers.py`
- `materiales/serializers.py`
- `inventario/serializers.py`
- `agenda/serializers.py`

### Archivos de API Views
- `usuarios/api_views.py`
- `tenants/api_views.py`
- `clientes/api_views.py`
- `pedidos/api_views.py`
- `contratos/api_views.py`
- `produccion/api_views.py`
- `materiales/api_views.py`
- `inventario/api_views.py`
- `agenda/api_views.py`

### Archivos de URLs de API
- `usuarios/api_urls.py`
- `tenants/api_urls.py`
- `clientes/api_urls.py`
- `pedidos/api_urls.py`
- `contratos/api_urls.py`
- `produccion/api_urls.py`
- `materiales/api_urls.py`
- `inventario/api_urls.py`
- `agenda/api_urls.py`

## Criterios de Aceptación

### Funcionalidad
- Todos los endpoints funcionan correctamente
- CRUD completo implementado
- Filtrado por tenant funcionando
- Paginación implementada
- Filtros y búsquedas funcionando

### Calidad de Código
- Serializers bien estructurados
- ViewSets optimizados
- Código reutilizable
- Documentación clara

### Seguridad
- Filtrado por tenant en todas las operaciones
- Validación de entrada
- Manejo seguro de errores
- No exposición de datos sensibles

### Performance
- Consultas optimizadas
- Paginación eficiente
- Filtros rápidos
- Respuestas rápidas

## Notas Importantes

### Dependencias
- Usar Django REST Framework
- Los modelos ya están creados
- Coordinar con equipo de autenticación para tokens
- Coordinar con equipo de configuración para URLs globales

### Comunicación
- Informar al equipo de configuración sobre rutas API
- Coordinar con equipo de autenticación para seguridad
- Mantener comunicación con equipo de vistas

### Testing
- Probar todos los endpoints
- Verificar filtrado por tenant
- Probar paginación y filtros
- Validar respuestas JSON
- Probar manejo de errores

## Recursos de Referencia

### Django REST Framework
- Serializers
- ViewSets
- APIViews
- Pagination
- Filtering
- Authentication

### Estructura del Proyecto
- Revisar modelos existentes
- Entender relaciones entre modelos
- Conocer campos disponibles

### Ejemplos de Implementación
- Usar patrones estándar de DRF
- Seguir convenciones del proyecto
- Mantener consistencia entre módulos
