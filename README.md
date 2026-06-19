# Sistema de Gestión Comercial — Bomberos Voluntarios de Cali

## Descripción del Proyecto

Este repositorio contiene el desarrollo del proyecto académico de Bases de Datos para el diseño e implementación de un Sistema de Gestión Comercial inspirado en el Benemérito Cuerpo de Bomberos Voluntarios de Cali.

El proyecto busca modelar y gestionar los procesos relacionados con:

- Clientes  
- Productos  
- Inventario  
- Proveedores  
- Órdenes de venta  
- Facturación  
- Pagos  
- Entregas  
- Órdenes de compra a proveedores  

Durante el desarrollo se realizaron las etapas de:

- Modelado conceptual  
- Diseño lógico  
- Normalización  
- Implementación física en PostgreSQL  

---

## Empresa de Referencia

El Benemérito Cuerpo de Bomberos Voluntarios de Cali es una institución fundada el 20 de julio de 1928.

Además de sus funciones de atención de emergencias, cuenta con una línea comercial dedicada a la venta de productos de seguridad industrial y prestación de servicios relacionados con prevención y protección contra incendios.

Sitio web: https://www.bomberoscali.org.co

---

## Integrantes

| Nombre | Código |
|--------|--------|
| Dana Sofía Gomez Manrique | 2438171 |
| Hilary Herrera Erazo | 2438987 |
| Laura Valentina Bernal Lozada | 2437088 |

---


## Modelo de Datos

El sistema está compuesto por las siguientes entidades principales:

- CLIENTE  
- PRODUCTO  
- INVENTARIO  
- ORDEN  
- DETALLE_ORDEN  
- FACTURA  
- PAGO  
- ENTREGA  
- EMPLEADO  
- SEDE  
- PROVEEDOR  
- ORDEN_PROVEEDOR  
- DETALLE_ORD_PROVEEDOR  

**Total: 13 tablas**

---

## Implementación en PostgreSQL
### 1. Crear la base de datos

```sql
CREATE DATABASE bomberos_cali;
```

### 2. Clonar el repositorio

```bash
git clone https://github.com/LauraBernal18/SGE-Bomberos-Cali-BD
cd SGE-Bomberos-Cali-BD
```

### 3. Ejecutar el script de creación de tablas
Desde IntelliJ IDEA:

- Abrir el proyecto clonado.
- Configurar la conexión a PostgreSQL.
- Abrir el archivo `db/ddl.sql`.
- Ejecutar el script.

### 4. Cargar los datos de prueba

- Abrir el archivo `db/inserts.sql`.
- Ejecutar el script.

### 5. Ejecutar las consultas de validación

- Abrir el archivo `db/consultas.sql`.
- Ejecutar el script.


