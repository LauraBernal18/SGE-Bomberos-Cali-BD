from django.db import models
from apps.clientes.models import Cliente

class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "sede"

    def __str__(self):
        return self.nombre_sede


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=100, unique=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    id_sede = models.ForeignKey(Sede, on_delete=models.DO_NOTHING, db_column="id_sede")

    class Meta:
        managed = False
        db_table = "empleado"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Orden(models.Model):
    ESTADOS = [
        ("En Proceso", "En Proceso"),
        ("Entregada", "Entregada"),
        ("Cancelada", "Cancelada"),
    ]

    id_orden = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column="id_cliente")
    id_empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column="id_empleado")
    id_sede = models.ForeignKey(Sede, on_delete=models.DO_NOTHING, db_column="id_sede")

    class Meta:
        managed = False
        db_table = "orden"

    def __str__(self):
        return f"Orden #{self.id_orden}"