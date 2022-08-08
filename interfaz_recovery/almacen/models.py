from django.db import models

# Create your models here.
class Recurso(models.Model):
    nombre = models.CharField(max_length=50)
    cod_seot = models.CharField(max_length=50)
    cod_forcebeat = models.CharField(max_length=50)
    cod_scm = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    cod_fb_tecnico = models.CharField(max_length=50)
    cod_seot_tecnico = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Tecnico"
        verbose_name_plural = "Tecnicos"

class SolMaterial(models.Model):
    cod_material = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cod_material.nombre + "____" + self.tecnico.nombre + "_____" + str(self.cantidad) 
    class Meta:
        verbose_name = "Solicitud de Material"
        verbose_name_plural = "Solicitudes de Material"
    