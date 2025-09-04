# 📸 FotoStudio - Sistema de Gestión para Negocio de Fotografía y Enmarcado

Un sistema web completo para la gestión integral de un negocio de fotografía profesional, enmarcado y servicios fotográficos especializados. El proyecto incluye módulos para gestión de pedidos, clientes, inventario, producción, agenda y reportes financieros.

## 🚀 Características Principales

- **Dashboard Interactivo**: Panel de control con métricas en tiempo real y gráficos estadísticos
- **Gestión de Pedidos**: Control completo del flujo de pedidos desde creación hasta entrega
- **Administración de Clientes**: Base de datos de clientes particulares y corporativos (colegios)
- **Control de Inventario**: Seguimiento detallado de materiales, varillas, pinturas y productos terminados
- **Órdenes de Producción**: Planificación y seguimiento de la producción de marcos y productos
- **Agenda Digital**: Programación de citas y seguimiento de entregas
- **Reportes Avanzados**: Análisis financiero con gráficos interactivos
- **Sistema Responsivo**: Interfaz adaptable para dispositivos móviles y desktop

## 📁 Estructura del Proyecto

```
MiniLabFrontend/
├── 📄 index.html                          # Página de redirección al login
├── 📄 README.md                           # Este archivo
├── 📂 assets/                             # Recursos estáticos
│   ├── 📂 css/                            # Hojas de estilo
│   │   ├── styles.css                     # Estilos globales del sistema
│   │   ├── login.css                      # Estilos específicos del login
│   │   ├── index.css                      # Estilos del dashboard
│   │   ├── pedidos.css                    # Estilos de gestión de pedidos
│   │   ├── clientes.css                   # Estilos de gestión de clientes
│   │   ├── contratos.css                  # Estilos de contratos
│   │   ├── inventario.css                 # Estilos del inventario
│   │   ├── orden-produccion.css           # Estilos de órdenes de producción
│   │   ├── produccion.css                 # Estilos de producción
│   │   ├── agenda.css                     # Estilos de la agenda
│   │   ├── reportes.css                   # Estilos de reportes
│   │   └── configuracion.css              # Estilos de configuración
│   └── 📂 js/                             # Scripts JavaScript
│       ├── index.js                       # Lógica del dashboard y gráficos
│       ├── pedidos.js                     # Funcionalidad de pedidos
│       ├── clientes.js                    # Gestión de clientes
│       ├── contratos.js                   # Manejo de contratos
│       ├── inventario.js                  # Control de inventario
│       ├── produccion.js                  # Gestión de producción
│       ├── agenda.js                      # Funcionalidad de agenda
│       ├── reportes.js                    # Generación de reportes
│       ├── configuracion.js               # Configuraciones del sistema
│       └── tienda-almacen.js              # Gestión de tienda/almacén
├── 📂 pages/                              # Páginas HTML del sistema
│   ├── login.html                         # Página de autenticación
│   ├── index.html                         # Dashboard principal
│   ├── pedidos.html                       # Gestión de pedidos
│   ├── clientes.html                      # Administración de clientes
│   ├── contratos.html                     # Gestión de contratos
│   ├── inventario.html                    # Control de inventario
│   ├── orden-produccion.html              # Órdenes de producción
│   ├── productos-terminados.html          # Productos terminados
│   ├── agenda.html                        # Agenda y citas
│   ├── reportes.html                      # Reportes y estadísticas
│   ├── configuracion.html                 # Configuración del sistema
│   ├── 📂 api/                            # APIs y servicios
│   │   └── 📂 inventario/                 # APIs específicas de inventario
│   │       ├── index.js                   # API principal de inventario
│   │       ├── alertas.js                 # Gestión de alertas de stock
│   │       ├── pinturas.js                # API de pinturas y acabados
│   │       ├── resumen.js                 # Resúmenes de inventario
│   │       └── varillas.js                # Gestión de varillas
│   └── 📂 inventario/                     # Módulo específico de inventario
│       └── index.js                       # Lógica del inventario
├── 📂 models/                             # Modelos de datos
│   ├── Cuadro.js                          # Modelo de cuadros/marcos
│   ├── Inventory.js                       # Modelos de inventario
│   ├── MovimientoInventario.js            # Historial de movimientos
│   └── Production.js                      # Modelos de producción
└── 📂 services/                           # Servicios de negocio
    ├── InventoryService.js                # Servicio de inventario
    └── ProductionService.js               # Servicio de producción
```

## 🛠️ Tecnologías Utilizadas

### Frontend
- **HTML5**: Estructura semántica de las páginas
- **CSS3**: Estilos avanzados con variables CSS y diseño responsivo
- **JavaScript (ES6+)**: Funcionalidad interactiva del cliente
- **Chart.js**: Gráficos interactivos para reportes y dashboard
- **Font Awesome**: Iconografía profesional

### Backend/Modelos (Preparado para)
- **Node.js**: Runtime de JavaScript
- **MongoDB**: Base de datos NoSQL
- **Mongoose**: ODM para MongoDB

### Características de Diseño
- **Diseño Responsivo**: Compatible con dispositivos móviles y desktop
- **Interfaz Moderna**: UI/UX contemporáneo con paleta de colores profesional
- **Navegación Intuitiva**: Menú lateral colapsible y navegación móvil optimizada
- **Sistema de Alertas**: Notificaciones visuales para stock bajo y eventos importantes

## 🎨 Paleta de Colores

El sistema utiliza una paleta de colores profesional definida en variables CSS:

```css
/* Colores principales */
--primary: #345291        /* Azul corporativo */
--secondary: #a74a4a      /* Rojo complementario */

/* Colores de estado */
--success: #4ca764        /* Verde para éxito */
--warning: #e8b842        /* Amarillo para advertencias */
--danger: #e84242         /* Rojo para errores */
--info: #42a5e8          /* Azul para información */
```

## 📋 Módulos del Sistema

### 1. 🏠 Dashboard
- **Métricas en tiempo real**: Pedidos nuevos, en producción, entregados
- **Alertas de inventario**: Stock bajo y productos críticos
- **Gráficos estadísticos**: Ingresos por servicio con Chart.js
- **Pedidos recientes**: Vista rápida de últimas transacciones

### 2. 📝 Gestión de Pedidos
- **CRUD completo**: Crear, leer, actualizar y eliminar pedidos
- **Estados de pedido**: Nuevo, En Producción, Entregado, Cancelado
- **Filtros avanzados**: Por cliente, tipo de servicio, estado, fecha
- **Tipos de servicio**:
  - Impresión Minilab
  - Recordatorios Escolares
  - Enmarcado
  - Retoque Fotográfico

### 3. 👥 Administración de Clientes
- **Clientes particulares**: Datos personales y historial
- **Clientes corporativos**: Colegios y empresas
- **Historial de pedidos**: Seguimiento completo por cliente
- **Datos de contacto**: Información completa y actualizable

### 4. 📋 Gestión de Contratos
- **Contratos escolares**: Campañas fotográficas en colegios
- **Seguimiento de estados**: Activos, vencidos, renovaciones
- **Términos y condiciones**: Gestión de clausulado

### 5. 📦 Control de Inventario
**Materiales para Enmarcado:**
- Varillas/Molduras de diferentes tipos y medidas
- Pinturas y acabados para marcos
- Control de stock mínimo y alertas automáticas

**Materiales de Impresión:**
- Papel fotográfico (diferentes tamaños)
- Químicos para revelado
- Tintas y consumibles

**Materiales para Recordatorios:**
- Materiales especializados para productos escolares
- Plantillas y diseños

**Servicios Artísticos:**
- Software y equipos para restauración digital
- Materiales para pintura al óleo
- Herramientas de diseño gráfico

### 6. 🏭 Órdenes de Producción
- **Planificación de producción**: Órdenes detalladas con materiales
- **Estados de orden**: Abierta, En Proceso, Cerrada, Cancelada
- **Control de merma**: Seguimiento de desperdicios y optimización
- **Asignación de responsables**: Control de quien ejecuta cada orden

### 7. ✅ Productos Terminados
- **Inventario de productos listos**: Control de stock final
- **Seguimiento de calidad**: Estados y observaciones
- **Preparación para entrega**: Gestión de productos terminados

### 8. 📅 Agenda Digital
- **Programación de citas**: Para sesiones fotográficas
- **Recordatorios de entrega**: Seguimiento de fechas importantes
- **Calendario interactivo**: Vista mensual y semanal

### 9. 📊 Reportes y Estadísticas
- **Reportes financieros**: Ingresos por servicio y período
- **Gráficos interactivos**: Visualización de datos con Chart.js
- **Análisis de rentabilidad**: Por tipo de servicio
- **Reportes de inventario**: Stock, movimientos, alertas

### 10. ⚙️ Configuración
- **Parámetros del sistema**: Configuraciones generales
- **Gestión de usuarios**: Roles y permisos
- **Configuración de alertas**: Umbrales de stock mínimo

## 🚀 Instalación y Configuración

### Requisitos Previos
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Servidor web local (opcional para desarrollo)

### Instalación
1. **Clonar o descargar el proyecto**:
   ```bash
   git clone [url-del-repositorio]
   cd MiniLabFrontend
   ```

2. **Abrir en navegador**:
   - Abrir `index.html` directamente en el navegador
   - O usar un servidor local como Live Server de VS Code

3. **Acceso al sistema**:
   - La página principal redirige automáticamente a `pages/login.html`
   - Usar cualquier credencial para acceder (no hay validación en el prototipo)

## 📱 Uso del Sistema

### Navegación
- **Menú lateral**: Navegación principal en dispositivos desktop
- **Menú móvil**: Hamburguesa en la parte superior para dispositivos móviles
- **Breadcrumbs**: Navegación contextual en cada módulo

### Funcionalidades Principales
1. **Login**: Acceso al sistema (sin validación real en prototipo)
2. **Dashboard**: Vista general del estado del negocio
3. **Gestión de datos**: CRUD completo en todos los módulos
4. **Reportes**: Visualización de estadísticas y métricas
5. **Configuración**: Personalización del sistema

## 🔧 Desarrollo y Personalización

### Estructura de Archivos CSS
- `styles.css`: Estilos globales y variables CSS
- Archivos específicos por módulo para mejor organización
- Sistema de variables CSS para fácil personalización

### JavaScript Modular
- Archivos JS separados por funcionalidad
- Uso de ES6+ para mejor legibilidad
- Integración con Chart.js para gráficos

### Responsividad
- Mobile-first approach
- Breakpoints optimizados para diferentes dispositivos
- Menús adaptativos según el tamaño de pantalla

## 📈 Características Avanzadas

### Gráficos y Visualizaciones
- **Chart.js**: Gráficos de torta, barras y líneas
- **Métricas en tiempo real**: Actualización dinámica de datos
- **Exportación de reportes**: Funcionalidad preparada para PDF/Excel

### Sistema de Alertas
- **Alertas de stock**: Notificaciones automáticas de stock bajo
- **Estados visuales**: Badges y colores para diferentes estados
- **Notificaciones**: Sistema de alertas en el dashboard

### Optimizaciones
- **Carga diferida**: Optimización de recursos
- **Cache de datos**: Mejora en rendimiento
- **Compresión**: Assets optimizados

## 🔮 Próximas Funcionalidades

### Backend Integration
- [ ] Conexión con API REST
- [ ] Base de datos MongoDB
- [ ] Autenticación y autorización real
- [ ] Validación de formularios

### Funcionalidades Avanzadas
- [ ] Sistema de notificaciones push
- [ ] Integración con sistemas de pago
- [ ] Generación automática de facturas
- [ ] Backup automático de datos
- [ ] Multi-idioma (internacionalización)

### Mejoras de UX/UI
- [ ] Tema oscuro/claro
- [ ] Animaciones y transiciones mejoradas
- [ ] Drag & drop para reorganización
- [ ] Búsqueda global inteligente

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear rama para nueva funcionalidad
3. Implementar cambios con tests
4. Crear Pull Request con descripción detallada

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

## 📞 Soporte

Para soporte técnico o consultas:
- **Documentación**: Revisar este README y comentarios en el código
- **Issues**: Reportar problemas en el sistema de issues del repositorio
- **Mejoras**: Sugerir nuevas funcionalidades via Pull Requests

---

## 🏆 Estado del Proyecto

**Versión**: 1.0.0 (Prototipo Frontend)
**Estado**: ✅ Completado - Prototipo funcional
**Última actualización**: Diciembre 2024

### Funcionalidades Implementadas ✅
- [x] Sistema de login (interfaz)
- [x] Dashboard con métricas
- [x] Gestión completa de pedidos
- [x] Administración de clientes
- [x] Control de inventario
- [x] Órdenes de producción
- [x] Agenda digital
- [x] Reportes con gráficos
- [x] Diseño responsivo
- [x] Navegación completa

### En Desarrollo 🔄
- [ ] Integración con backend
- [ ] Validaciones de formularios
- [ ] Persistencia de datos
- [ ] Sistema de autenticación real

---

*Desarrollado con ❤️ para optimizar la gestión de negocios fotográficos profesionales.* 