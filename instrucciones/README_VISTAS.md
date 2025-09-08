# Equipo de Vistas - Instrucciones de Desarrollo

## Responsabilidad Principal
Construir las vistas en Django para el sistema de gestión empresarial multi-tenant.

## Alcance de Trabajo

### ✅ Tareas Incluidas
- Crear vistas basadas en clases para cada módulo
- Implementar endpoints de prueba que devuelvan datos simples
- Consumir los modelos existentes sin modificarlos
- Mantener diseño escalable y reutilizable

### ❌ Tareas Excluidas
- Modificar configuración global del proyecto
- Crear APIs (eso es responsabilidad del equipo API)
- Modificar modelos existentes
- Configurar autenticación (responsabilidad del equipo de autenticación)

## Módulos a Desarrollar

### 1. Gestión de Tenants
**Archivo**: `tenants/views.py`
- Vista para listar todos los tenants
- Vista para mostrar detalles de un tenant específico
- Vista para crear nuevo tenant
- Vista para actualizar información del tenant
- Vista para cambiar estado del tenant

### 2. Gestión de Usuarios
**Archivo**: `usuarios/views.py`
- Vista para listar usuarios del tenant actual
- Vista para mostrar perfil de usuario
- Vista para crear nuevo usuario
- Vista para actualizar datos de usuario
- Vista para gestionar grupos de usuarios

### 3. Gestión de Clientes
**Archivo**: `clientes/views.py`
- Vista para listar clientes del tenant
- Vista para mostrar detalles del cliente
- Vista para crear nuevo cliente
- Vista para actualizar información del cliente
- Vista para buscar clientes

### 4. Gestión de Pedidos
**Archivo**: `pedidos/views.py`
- Vista para listar pedidos del tenant
- Vista para mostrar detalles del pedido
- Vista para crear nuevo pedido
- Vista para actualizar pedido
- Vista para cambiar estado del pedido
- Vista para gestionar detalles del pedido

### 5. Gestión de Contratos
**Archivo**: `contratos/views.py`
- Vista para listar contratos del tenant
- Vista para mostrar detalles del contrato
- Vista para crear nuevo contrato
- Vista para actualizar contrato
- Vista para cambiar estado del contrato

### 6. Gestión de Producción
**Archivo**: `produccion/views.py`
- Vista para listar órdenes de producción
- Vista para mostrar detalles de orden
- Vista para crear nueva orden
- Vista para gestionar varillas
- Vista para gestionar cuadros
- Vista para movimientos de inventario

### 7. Gestión de Materiales
**Archivo**: `materiales/views.py`
- Vista para pintura y acabados
- Vista para materiales de impresión
- Vista para materiales recordatorio
- Vista para software y equipos
- Vista para materiales de pintura
- Vista para materiales de diseño
- Vista para productos terminados

### 8. Gestión de Inventario
**Archivo**: `inventario/views.py`
- Vista para listar inventario general
- Vista para mostrar inventario por tipo
- Vista para alertas de stock mínimo
- Vista para reportes de inventario

### 9. Gestión de Agenda
**Archivo**: `agenda/views.py`
- Vista para listar eventos del tenant
- Vista para mostrar detalles del evento
- Vista para crear nuevo evento
- Vista para actualizar evento
- Vista para cambiar estado del evento
- Vista para calendario por fecha

## Estructura de Vistas Requerida

### Vista de Lista (ListView)
- Mostrar todos los elementos del tenant
- Incluir paginación básica
- Filtrar por tenant_id automáticamente
- Devolver datos en formato simple

### Vista de Detalle (DetailView)
- Mostrar información completa de un elemento
- Verificar que pertenece al tenant actual
- Incluir datos relacionados básicos

### Vista de Creación (CreateView)
- Formulario para crear nuevos elementos
- Asignar automáticamente tenant_id
- Validación básica de datos
- Redirección después de crear

### Vista de Actualización (UpdateView)
- Formulario para editar elementos existentes
- Verificar permisos de tenant
- Validación de datos
- Redirección después de actualizar

### Vista de Eliminación (DeleteView)
- Confirmación de eliminación
- Verificar permisos de tenant
- Eliminación segura
- Redirección después de eliminar

## Consideraciones Técnicas

### Filtrado por Tenant
- Todas las vistas deben filtrar automáticamente por tenant_id
- No mostrar datos de otros tenants
- Verificar permisos de acceso

### Manejo de Errores
- Implementar manejo básico de errores
- Mostrar mensajes informativos al usuario
- Redireccionar en caso de errores

### Templates Básicos
- Crear templates simples para cada vista
- Usar herencia de templates
- Incluir navegación básica
- Diseño responsive mínimo

### Formularios
- Crear formularios para cada modelo
- Validación básica de campos
- Manejo de archivos si es necesario
- Mensajes de éxito y error

## Entregables Esperados

### Archivos de Vistas
- `tenants/views.py` - Completamente implementado
- `usuarios/views.py` - Completamente implementado
- `clientes/views.py` - Completamente implementado
- `pedidos/views.py` - Completamente implementado
- `contratos/views.py` - Completamente implementado
- `produccion/views.py` - Completamente implementado
- `materiales/views.py` - Completamente implementado
- `inventario/views.py` - Completamente implementado
- `agenda/views.py` - Completamente implementado

### Templates Básicos
- Templates para listas, detalles, creación, edición y eliminación
- Template base común
- Navegación entre módulos

### Formularios
- Formularios para cada modelo
- Validación básica implementada
- Manejo de errores

## Criterios de Aceptación

### Funcionalidad
- Todas las vistas funcionan correctamente
- Filtrado por tenant implementado
- CRUD básico funcionando
- Navegación entre vistas

### Calidad de Código
- Código limpio y bien documentado
- Uso de vistas basadas en clases
- Reutilización de código
- Manejo de errores apropiado

### Seguridad
- Verificación de tenant en todas las operaciones
- No exposición de datos de otros tenants
- Validación de entrada de datos

## Notas Importantes

### Dependencias
- Los modelos ya están creados y no deben modificarse
- Usar solo las funcionalidades básicas de Django
- No implementar autenticación (eso es otro equipo)

### Comunicación
- Coordinar con el equipo de configuración para URLs
- Informar al equipo de APIs sobre estructura de datos
- Mantener comunicación con el equipo de autenticación

### Testing
- Probar todas las vistas manualmente
- Verificar filtrado por tenant
- Probar flujos completos de CRUD
- Validar manejo de errores

## Recursos de Referencia

### Documentación Django
- Django Class-Based Views
- Django Forms
- Django Templates
- Django Model Queries

### Estructura del Proyecto
- Revisar modelos existentes en cada app
- Entender relaciones entre modelos
- Conocer campos disponibles en cada modelo

### Ejemplos de Implementación
- Usar patrones estándar de Django
- Seguir convenciones del proyecto
- Mantener consistencia entre módulos
