-- ============================================================
-- CONSULTAS DE VALIDACIÓN - Avance 3
-- Sistema Bomberos Voluntarios de Cali
-- ============================================================

-- 1. Top 5 productos más vendidos (por cantidad total)
SELECT
    p.id_producto,
    p.nombre AS producto,
    p.categoria,
    SUM(d.cantidad) AS total_unidades_vendidas,
    SUM(d.subtotal) AS ingresos_totales
FROM PRODUCTO p
         JOIN DETALLE_ORDEN d ON p.id_producto = d.id_producto
         JOIN ORDEN o ON d.id_orden = o.id_orden
WHERE o.estado IN ('Entregada', 'En Proceso')
GROUP BY p.id_producto, p.nombre, p.categoria
ORDER BY total_unidades_vendidas DESC
    LIMIT 5;


-- 2. Ventas por sede: cuánto ha facturado cada sede
SELECT
    s.id_sede,
    s.nombre_sede,
    s.direccion,
    COUNT(o.id_orden) AS total_ordenes,
    SUM(o.total) AS total_facturado
FROM SEDE s
         JOIN ORDEN o ON s.id_sede = o.id_sede
WHERE o.estado != 'Cancelada'
GROUP BY s.id_sede, s.nombre_sede, s.direccion
ORDER BY total_facturado DESC;


-- 3. Estado del inventario con días de stock calculados en tiempo real
SELECT
    p.id_producto,
    p.nombre AS producto,
    p.categoria,
    i.stock_actual,
    i.demanda_diaria,
    i.estado_stock,
    CASE
        WHEN i.demanda_diaria = 0 THEN NULL
        ELSE ROUND((i.stock_actual::DECIMAL / i.demanda_diaria), 1)
        END AS dias_stock_calculados
FROM PRODUCTO p
         JOIN INVENTARIO i ON p.id_producto = i.id_producto
WHERE p.activo = TRUE
ORDER BY dias_stock_calculados ASC NULLS LAST;


-- 4. Clientes con mayor valor acumulado en órdenes
SELECT
    c.id_cliente,
    c.num_doc,
    c.nombre_razon_social,
    c.tipo_cliente,
    c.ciudad,
    COUNT(o.id_orden) AS total_ordenes,
    SUM(o.total) AS valor_total_compras
FROM CLIENTE c
         JOIN ORDEN o ON c.id_cliente = o.id_cliente
WHERE o.estado != 'Cancelada'
GROUP BY c.id_cliente, c.num_doc, c.nombre_razon_social, c.tipo_cliente, c.ciudad
ORDER BY valor_total_compras DESC
    LIMIT 10;


-- 5. Desempeño de empleados: cuántas órdenes gestionó cada uno y su valor total
SELECT
    e.id_empleado,
    e.nombre || ' ' || e.apellido AS empleado,
    e.cargo,
    s.nombre_sede,
    COUNT(o.id_orden) AS ordenes_gestionadas,
    SUM(o.total) AS valor_gestionado
FROM EMPLEADO e
         JOIN ORDEN o ON e.id_empleado = o.id_empleado
         JOIN SEDE s ON e.id_sede = s.id_sede
WHERE o.estado != 'Cancelada'
GROUP BY e.id_empleado, e.nombre, e.apellido, e.cargo, s.nombre_sede
ORDER BY valor_gestionado DESC;


-- 6. Facturas pendientes de pago (generadas pero sin pago en estado 'Pagado')
SELECT
    f.id_factura,
    f.num_consec,
    f.estado_factura,
    f.total AS valor_factura,
    f.fecha_generacion,
    c.nombre_razon_social AS cliente,
    c.num_doc
FROM FACTURA f
         JOIN ORDEN o ON f.id_orden = o.id_orden
         JOIN CLIENTE c ON o.id_cliente = c.id_cliente
WHERE f.estado_factura = 'Generada'
  AND f.id_factura NOT IN (
    SELECT id_factura FROM PAGO WHERE estado_pago = 'Pagado'
)
ORDER BY f.fecha_generacion ASC;


-- 7. Proveedores con más órdenes de compra y su calificación
SELECT
    pv.id_proveedor,
    pv.nit,
    pv.razon_social,
    pv.calificacion,
    pv.tiempo_entrega AS dias_entrega_promedio,
    COUNT(op.id_ord_prov) AS total_ordenes_compra,
    SUM(op.total) AS total_comprado
FROM PROVEEDOR pv
         JOIN ORDEN_PROVEEDOR op ON pv.id_proveedor = op.id_proveedor
WHERE pv.activo = TRUE
  AND op.estado != 'Cancelada'
GROUP BY pv.id_proveedor, pv.nit, pv.razon_social, pv.calificacion, pv.tiempo_entrega
ORDER BY total_comprado DESC;


-- 8. Productos por proveedor con su nivel de inventario actual
SELECT
    pv.razon_social AS proveedor,
    p.id_producto,
    p.nombre AS producto,
    p.precio,
    i.stock_actual,
    i.estado_stock
FROM PROVEEDOR pv
         JOIN PRODUCTO p ON pv.id_proveedor = p.id_proveedor
         JOIN INVENTARIO i ON p.id_producto = i.id_producto
WHERE p.activo = TRUE
  AND pv.activo = TRUE
ORDER BY pv.razon_social, i.estado_stock;


-- 9. Entregas pendientes o en ruta con datos del cliente y empleado responsable
SELECT
    en.id_entrega,
    en.estado_entrega,
    en.fecha_llegada,
    en.direccion_entrega,
    c.nombre_razon_social AS cliente,
    c.telefono AS telefono_cliente,
    e.nombre || ' ' || e.apellido AS empleado_entrega
FROM ENTREGA en
         JOIN ORDEN o ON en.id_orden = o.id_orden
         JOIN CLIENTE c ON o.id_cliente = c.id_cliente
         JOIN EMPLEADO e ON en.id_empleado = e.id_empleado
WHERE en.estado_entrega IN ('Pendiente', 'En Ruta')
ORDER BY en.fecha_llegada ASC;


-- 10. Análisis mensual de ventas: ingresos por mes con conteo de facturas
SELECT
    EXTRACT(YEAR FROM f.fecha_generacion) AS anio,
    EXTRACT(MONTH FROM f.fecha_generacion) AS mes,
    TO_CHAR(f.fecha_generacion, 'Month YYYY') AS periodo,
    COUNT(f.id_factura) AS total_facturas,
    SUM(f.subtotal) AS subtotal_sin_iva,
    SUM(f.total_iva) AS total_iva_recaudado,
    SUM(f.total) AS total_ingresos
FROM FACTURA f
WHERE f.estado_factura IN ('Generada', 'Pagada')
GROUP BY
    EXTRACT(YEAR FROM f.fecha_generacion),
    EXTRACT(MONTH FROM f.fecha_generacion),
    TO_CHAR(f.fecha_generacion, 'Month YYYY')
ORDER BY anio, mes;