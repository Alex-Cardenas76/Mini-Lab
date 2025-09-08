# Sistema de Gestión Empresarial Multi-tenant

## Descripción General

Este es un sistema de gestión empresarial desarrollado en Django que implementa una arquitectura multi-tenant para manejar múltiples empresas o clientes de forma independiente. El sistema está diseñado específicamente para empresas que se dedican a la producción de cuadros y varillas, incluyendo gestión de inventario, pedidos, contratos y producción.

## Características Principales

### �� Arquitectura Multi-tenant
- **Sistema de Tenants**: Cada empresa cliente tiene su propio espacio aislado
- **Aislamiento de Datos**: Todos los datos están separados por `tenant_id`
- **Gestión de Usuarios**: Sistema de autenticación personalizado con roles y permisos

### 📋 Módulos del Sistema

#### 1. **Gestión de Tenants** (`tenants/`)
- Administración de empresas cliente
- Configuración de subdominios únicos
- Estados: activo, inactivo, suspendido

#### 2. **Gestión de Usuarios** (`usuarios/`)
- Sistema de autenticación personalizado
- Tipos de documentos de identidad
- Grupos y permisos de usuario
- Códigos de verificación y seguridad
- Gestión de sesiones y tokens

#### 3. **Gestión de Clientes** (`clientes/`)
- Registro de clientes (personas, empresas, otros)
- Información de contacto completa
- Historial de transacciones

#### 4. **Gestión de Contratos** (`contratos/`)
- Creación y seguimiento de contratos
- Estados: vigente, vencido, rescindido
- Control de montos y fechas

#### 5. **Gestión de Pedidos** (`pedidos/`)
- Procesamiento de pedidos de clientes
- Detalles de pedidos con múltiples tipos de items
- Estados: pendiente, en proceso, entregado, cancelado
- Cálculo automático de totales

#### 6. **Gestión de Inventario** (`inventario/`)
- Control de stock en tiempo real
- Alertas de stock mínimo
- Ubicación de productos
- Seguimiento de movimientos

#### 7. **Gestión de Materiales** (`materiales/`)
- **Pintura y Acabados**: Colores, tipos, precios
- **Materiales de Impresión**: Especificaciones técnicas
- **Materiales Recordatorio**: Productos promocionales
- **Software y Equipos**: Licencias y versiones
- **Materiales de Pintura**: Insumos para producción
- **Materiales de Diseño**: Herramientas creativas
- **Productos Terminados**: Cuadros finalizados
- **Varillas**: Materia prima principal

#### 8. **Gestión de Producción** (`produccion/`)
- **Órdenes de Producción**: Planificación de trabajos
- **Varillas**: Materia prima con especificaciones
- **Cuadros**: Productos en proceso y terminados
- **Detalles de Órdenes**: Seguimiento de producción
- **Movimientos de Inventario**: Entradas, salidas, ajustes

#### 9. **Agenda** (`agenda/`)
- Gestión de citas y eventos
- Estados: pendiente, confirmada, completada, cancelada
- Asignación por usuario y tenant

## Estructura de la Base de Datos

### Tablas Principales

#### Gestión Multi-tenant
- `Tenant`: Información de empresas cliente
- `users`: Sistema de usuarios personalizado
- `auth_group`, `auth_permission`: Roles y permisos

#### Gestión Comercial
- `Cliente`: Base de datos de clientes
- `Contrato`: Contratos y acuerdos
- `Pedido`, `DetallePedido`: Órdenes de compra

#### Gestión de Inventario
- `Inventario`: Control general de stock
- `PinturaAcabado`: Productos de acabado
- `MaterialImpresion`: Materiales de impresión
- `MaterialRecordatorio`: Productos promocionales
- `SoftwareEquipo`: Licencias y equipos
- `MaterialPintura`: Insumos de pintura
- `MaterialDiseno`: Herramientas de diseño
- `ProductoTerminado`: Cuadros finalizados
- `Varilla`: Materia prima principal

#### Gestión de Producción
- `OrdenProduccion`: Órdenes de trabajo
- `DetalleOrden`: Detalles de producción
- `Cuadro`: Productos en proceso
- `MovimientoInventario`: Historial de movimientos
- `MaterialVarilla`: Relación materiales-varillas

#### Gestión Operativa
- `Agenda`: Citas y eventos
- `DocumentTypes`: Tipos de documentos
- `UsersVerificationCode`: Códigos de seguridad

## Tecnologías Utilizadas

- **Backend**: Django 5.2.6
- **Base de Datos**: MySQL
- **API**: Django REST Framework 3.16.1
- **Autenticación**: Sistema personalizado multi-tenant
- **Arquitectura**: Multi-tenant con aislamiento por tenant_id

## Configuración del Proyecto

### Estructura de Directorios

av1-orginal/
    ├── config/ # Configuración principal de Django
    ├── agenda/ # Módulo de agenda y citas
    ├── clientes/ # Gestión de clientes
    ├── contratos/ # Gestión de contratos
    ├── inventario/ # Control de inventario
    ├── materiales/ # Gestión de materiales
    ├── pedidos/ # Gestión de pedidos
    ├── produccion/ # Gestión de producción
    ├── tenants/ # Gestión multi-tenant
    ├── usuarios/ # Sistema de usuarios
    └── venv/ # Entorno virtual



### Configuración de Django
- **DEBUG**: Habilitado para desarrollo
- **Base de Datos**: SQLite3
- **Idioma**: Inglés (configurable)
- **Zona Horaria**: UTC
- **Aplicaciones**: Solo Django core (las apps personalizadas no están registradas aún)

## Características Técnicas

### Modelos de Datos
- **Aislamiento Multi-tenant**: Todos los modelos incluyen `tenant_id`
- **Auditoría**: Campos `created_at` y `updated_at` en todos los modelos
- **Estados**: Sistemas de estados para control de flujo
- **Relaciones**: Referencias por ID para flexibilidad

### Seguridad
- **Aislamiento de Datos**: Separación completa por tenant
- **Autenticación Personalizada**: Sistema propio de usuarios
- **Permisos**: Sistema de grupos y permisos granular
- **Verificación**: Códigos de verificación con intentos limitados

### Escalabilidad
- **Arquitectura Multi-tenant**: Soporte para múltiples empresas
- **Base de Datos Optimizada**: Índices y relaciones eficientes
- **Modularidad**: Aplicaciones independientes y reutilizables

## Estado del Proyecto

### ✅ Completado
- Estructura base del proyecto Django
- Modelos de datos completos
- Arquitectura multi-tenant
- Sistema de usuarios personalizado
- Gestión de inventario y materiales
- Sistema de producción
- Gestión comercial (clientes, contratos, pedidos)

### �� Pendiente
- Registro de aplicaciones en `settings.py`
- Configuración de URLs
- Vistas y APIs
- Interfaz de usuario
- Migraciones de base de datos
- Configuración de producción

## Instalación y Configuración

### Requisitos
- Python 3.10+
- Django 5.2.6
- Django REST Framework 3.16.1

### Pasos de Instalación
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno virtual
4. Instalar dependencias: `pip install -r requirements.txt`
5. Configurar base de datos
6. Ejecutar migraciones: `python manage.py migrate`
7. Crear superusuario: `python manage.py createsuperuser`
8. Ejecutar servidor: `python manage.py runserver`

## Uso del Sistema

### Gestión Multi-tenant
1. Crear tenant (empresa cliente)
2. Configurar subdominio único
3. Asignar usuarios al tenant
4. Configurar permisos y roles

### Flujo de Trabajo
1. **Registro de Clientes**: Crear y gestionar base de clientes
2. **Gestión de Contratos**: Establecer acuerdos comerciales
3. **Procesamiento de Pedidos**: Recibir y procesar órdenes
4. **Planificación de Producción**: Crear órdenes de trabajo
5. **Control de Inventario**: Gestionar stock y materiales
6. **Seguimiento de Producción**: Monitorear avance de trabajos
7. **Entrega y Facturación**: Completar ciclo comercial
