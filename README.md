# 📸 FotoStudio - Sistema Django de Gestión para Negocio de Fotografía y Enmarcado

Un sistema web Django completo para la gestión integral de un negocio de fotografía profesional, enmarcado y servicios fotográficos especializados. El proyecto incluye módulos para gestión de pedidos, clientes, inventario, producción, agenda y reportes financieros con soporte multi-tenant.

## 🚀 Características Principales

- **Dashboard Interactivo**: Panel de control con métricas en tiempo real
- **Gestión de Pedidos**: Control completo del flujo de pedidos desde creación hasta entrega
- **Administración de Clientes**: Base de datos de clientes particulares y corporativos (colegios)
- **Control de Inventario**: Seguimiento detallado de materiales, varillas, pinturas y productos terminados
- **Órdenes de Producción**: Planificación y seguimiento de la producción de marcos y productos
- **Agenda Digital**: Programación de citas y seguimiento de entregas
- **Reportes Avanzados**: Análisis financiero con métricas detalladas
- **Multi-Tenant**: Soporte para múltiples empresas en una sola instalación
- **Sistema Responsivo**: Interfaz adaptable para dispositivos móviles y desktop

## 🏗️ Arquitectura del Proyecto

### Estructura Django

```
fotostudio_system/
├── 📁 apps/                                    # Apps del proyecto organizadas
│   ├── 📁 core/                               # App principal con modelos base
│   │   ├── models.py                          # Modelos base y multi-tenant
│   │   ├── middleware/                        # Middleware personalizado
│   │   └── views.py                          # Vistas principales
│   ├── 📁 clientes/                          # Gestión de clientes
│   ├── 📁 pedidos/                           # Gestión de pedidos
│   ├── 📁 contratos/                         # Gestión de contratos
│   ├── 📁 inventario/                        # Control de inventario
│   ├── 📁 produccion/                        # Órdenes de producción
│   ├── 📁 agenda/                            # Agenda y citas
│   └── 📁 reportes/                          # Reportes y métricas
├── 📁 templates/                             # Templates organizados por app
│   ├── 📁 base/                              # Templates base
│   ├── 📁 auth/                              # Templates de autenticación
│   └── 📁 [app_name]/                        # Templates por app
├── 📁 static/                                # Archivos estáticos
│   └── 📁 css/                               # Hojas de estilo CSS
├── 📁 fotostudio_system/                     # Configuración del proyecto
│   ├── settings.py                           # Configuración Django
│   └── urls.py                              # URLs principales
├── manage.py                                 # Script de gestión Django
├── requirements.txt                          # Dependencias del proyecto
└── README.md                                 # Este archivo
```

### Apps Independientes

1. **`apps.core`**: Modelos base, middleware multi-tenant, vistas principales
2. **`apps.clientes`**: Gestión de clientes particulares y corporativos
3. **`apps.pedidos`**: Gestión completa de pedidos con diferentes tipos de servicio
4. **`apps.contratos`**: Contratos escolares y empresariales
5. **`apps.inventario`**: Control de stock de varillas, pinturas, materiales
6. **`apps.produccion`**: Órdenes de producción y productos terminados
7. **`apps.agenda`**: Eventos, citas y programación
8. **`apps.reportes`**: Métricas financieras y reportes

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 4.2**: Framework web principal
- **MySQL**: Base de datos principal
- **Python 3.8+**: Lenguaje de programación

### Frontend
- **HTML5**: Estructura semántica de las páginas
- **CSS3**: Estilos responsivos con variables CSS
- **Chart.js**: Gráficos interactivos para reportes (integrado en templates)
- **Font Awesome**: Iconografía profesional

### Características de Django
- **Multi-Tenant**: Soporte para múltiples tenants usando row-level security
- **Modelos Relacionales**: Estructura robusta con ForeignKeys y relaciones
- **Sistema de Autenticación**: Login/logout integrado
- **Middleware Personalizado**: Para manejo de multi-tenancy
- **Admin Interface**: Panel de administración de Django
- **ORM Avanzado**: Consultas optimizadas y relaciones complejas

## 📋 Módulos del Sistema

### 1. 🏠 Dashboard
- **Métricas en tiempo real**: Pedidos nuevos, en producción, entregados
- **Alertas de inventario**: Stock bajo y productos críticos
- **Gráficos estadísticos**: Ingresos por servicio
- **Pedidos recientes**: Vista rápida de últimas transacciones

### 2. 📝 Gestión de Pedidos
- **CRUD completo**: Crear, leer, actualizar y eliminar pedidos
- **Estados de pedido**: Nuevo, En Producción, Entregado, Cancelado
- **Tipos de servicio detallados**:
  - Impresión Minilab (con detalles de papel y cantidad)
  - Recordatorios Escolares (con plantillas y cantidades)
  - Enmarcado (con medidas y tipos de marco)
  - Retoque Fotográfico (con tipos de retoque)
- **Archivos adjuntos**: Soporte para subir archivos por pedido
- **Historial de estados**: Seguimiento completo de cambios

### 3. 👥 Administración de Clientes
- **Clientes particulares**: Datos personales completos
- **Clientes corporativos**: Colegios y empresas con contactos
- **Historial de interacciones**: Registro de llamadas, emails, visitas
- **Validaciones automáticas**: Según tipo de cliente

### 4. 📋 Gestión de Contratos
- **Contratos escolares**: Campañas fotográficas con detalles específicos
- **Contratos empresariales**: Servicios corporativos
- **Sistema de pagos**: Registro de pagos con documentos
- **Renovaciones automáticas**: Control de vencimientos
- **Documentos adjuntos**: Almacenamiento de contratos y anexos

### 5. 📦 Control de Inventario
**Sistema de Inventario Robusto:**
- **Varillas/Molduras**: Con medidas, materiales, colores
- **Pinturas y Acabados**: Clasificadas por tipo y color
- **Materiales de Impresión**: Papel fotográfico, químicos, tintas
- **Materiales para Recordatorios**: Suministros especializados
- **Movimientos de Inventario**: Historial completo de entradas/salidas
- **Alertas de Stock**: Notificaciones automáticas de stock bajo
- **Productos Terminados**: Control de productos listos para venta

### 6. 🏭 Órdenes de Producción
- **Planificación detallada**: Órdenes con materiales específicos
- **Estados de orden**: Abierta, En Proceso, Cerrada, Cancelada
- **Control de merma**: Seguimiento de desperdicios
- **Cuadros producidos**: Registro individual de productos
- **Control de calidad**: Evaluación de productos terminados
- **Historial de producción**: Registro de eventos y cambios

### 7. 📅 Agenda Digital
- **Eventos programados**: Sesiones fotográficas, entregas, reuniones
- **Recordatorios automáticos**: Configurables por evento
- **Gestión de recursos**: Salas, equipos, personal
- **Eventos recurrentes**: Programación automática
- **Historial de eventos**: Seguimiento de cambios

### 8. 📊 Reportes y Métricas
- **Métricas Financieras**: Ingresos por servicio, costos, utilidades
- **Métricas de Inventario**: Stock, movimientos, valorización
- **Métricas de Producción**: Eficiencia, merma, calidad
- **Reportes configurables**: Parámetros personalizables
- **Exportación**: PDF, Excel, CSV

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- MySQL 5.7 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone [url-del-repositorio]
   cd Mini-Lab
   ```

2. **Crear entorno virtual**:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Desarrollo con SQLite (Recomendado para empezar)**:
   ```bash
   # Aplicar migraciones con SQLite
   python manage.py makemigrations
   python manage.py migrate --settings=fotostudio_system.settings_dev
   
   # Crear superusuario (password: admin123)
   python manage.py createsuperuser --settings=fotostudio_system.settings_dev
   
   # Ejecutar servidor de desarrollo
   python manage.py runserver --settings=fotostudio_system.settings_dev
   ```

5. **Configurar base de datos MySQL (Producción)**:
   - Crear una base de datos llamada `fotostudio_db`
   - Configurar las variables de entorno o modificar `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'fotostudio_db',
           'USER': 'tu_usuario',
           'PASSWORD': 'tu_contraseña',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **Script de desarrollo rápido**:
   ```bash
   # Usar el script personalizado
   python run_dev.py runserver
   ```

9. **Acceder al sistema**:
   - Abrir navegador en `http://127.0.0.1:8000`
   - Usar las credenciales del superusuario creado

## 🔧 Configuración Multi-Tenant

### Variables de Entorno
Configurar las siguientes variables para personalizar el comportamiento:

```bash
# Base de datos
DB_NAME=fotostudio_db
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306

# Multi-tenant
TENANT_COOKIE_NAME=tenant_id
TENANT_HEADER_NAME=HTTP_X_TENANT_ID
```

### Configuración de Tenants
1. Acceder al admin de Django: `/admin/`
2. Crear registros en el modelo `Tenant`
3. Asociar usuarios a tenants usando `TenantUser`

## 📱 Uso del Sistema

### Navegación
- **Menú lateral**: Navegación principal en dispositivos desktop
- **Menú móvil**: Hamburguesa en la parte superior para dispositivos móviles
- **Breadcrumbs**: Navegación contextual en cada módulo

### Funcionalidades Principales
1. **Login**: Sistema de autenticación Django
2. **Dashboard**: Vista general del estado del negocio
3. **Gestión de datos**: CRUD completo en todos los módulos
4. **Reportes**: Métricas y análisis detallados
5. **Multi-tenant**: Separación automática de datos por tenant

## 🗄️ Estructura de Base de Datos

### Modelos Principales
- **Tenant**: Gestión de múltiples empresas
- **Cliente**: Particulares y corporativos
- **Pedido**: Con detalles específicos por tipo de servicio
- **Contrato**: Escolares y empresariales
- **Inventario**: Varillas, pinturas, materiales
- **OrdenProduccion**: Con detalles y cuadros producidos
- **EventoAgenda**: Programación y recordatorios
- **Métricas**: Financieras, inventario, producción

### Multi-Tenancy
- Todos los modelos incluyen `tenant_id`
- Middleware automático para filtrado
- Separación completa de datos por tenant

## 🔒 Seguridad

- **Autenticación requerida**: Todas las vistas protegidas
- **Multi-tenant**: Separación automática de datos
- **Validaciones**: En modelos y formularios
- **CSRF Protection**: Protección contra ataques CSRF
- **SQL Injection**: Protección mediante ORM de Django

## 🚧 Desarrollo

### Estructura de Código
- **Modelos**: Organizados por funcionalidad
- **Vistas**: CBV y FBV según necesidad
- **Templates**: Herencia y bloques reutilizables
- **URLs**: Namespaces por app
- **Middleware**: Personalizado para multi-tenancy

### Comandos Útiles
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear app nueva
python manage.py startapp nueva_app

# Shell de Django
python manage.py shell

# Ejecutar tests
python manage.py test
```

## 📈 Próximas Funcionalidades

### Mejoras Pendientes
- [ ] APIs REST con Django REST Framework
- [ ] Sistema de notificaciones en tiempo real
- [ ] Integración con sistemas de pago
- [ ] Generación automática de facturas
- [ ] Backup automático de datos
- [ ] Dashboard de métricas avanzado
- [ ] Integración con servicios de email/SMS

### Optimizaciones Técnicas
- [ ] Cache con Redis
- [ ] Optimización de consultas
- [ ] Tests automatizados
- [ ] CI/CD pipeline
- [ ] Monitoring y logging

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear rama para nueva funcionalidad
3. Implementar cambios siguiendo las convenciones Django
4. Crear Pull Request con descripción detallada

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

## 📞 Soporte

Para soporte técnico o consultas:
- **Documentación**: Este README y docstrings en el código
- **Issues**: Reportar problemas en el sistema de issues del repositorio
- **Django Admin**: Panel de administración en `/admin/`

---

## 🏆 Estado del Proyecto

**Versión**: 2.0.0 (Django Migration)
**Estado**: ✅ Migrado - Sistema Django funcional
**Última actualización**: Enero 2025

### Funcionalidades Implementadas ✅
- [x] Migración completa a Django
- [x] Sistema multi-tenant con row-level security
- [x] Modelos robustos con relaciones
- [x] Dashboard con métricas
- [x] Gestión completa de pedidos
- [x] Administración de clientes
- [x] Control de inventario avanzado
- [x] Órdenes de producción
- [x] Agenda digital
- [x] Sistema de reportes
- [x] Autenticación y autorización
- [x] Diseño responsivo
- [x] Conexión MySQL
- [x] Estructura escalable

### Cambios de la Migración 🔄
- ✅ Frontend estático → Django templates
- ✅ JavaScript → Python/Django logic
- ✅ Sin base de datos → MySQL con ORM
- ✅ Single-tenant → Multi-tenant
- ✅ Datos simulados → Modelos relacionales

---

*Desarrollado con ❤️ utilizando Django para optimizar la gestión de negocios fotográficos profesionales.*