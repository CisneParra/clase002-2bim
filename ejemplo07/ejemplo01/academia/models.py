from django.db import models
from datetime import date

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def __str__(self):
        anio_nacimiento = date.today().year - self.edad

        if self.cedula.startswith("11"):
            ciudad = "Loja"
        else:
            ciudad = "Otra ciudad"

        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {ciudad} - Edad: {self.edad} - Año de nacimiento: {anio_nacimiento}"