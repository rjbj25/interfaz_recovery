from django.db import models

# Create your models here.
class Recurso(models.Model):
    nombre = models.CharField(max_length=100)
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
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tecnico.nombre + " - " + self.fecha_hora.strftime("%d/%m/%Y %H:%M")
    class Meta:
        verbose_name = "Solicitud de Material"
        verbose_name_plural = "Solicitudes de Material"
    
class SolMaterialChoises(models.Model):
    cod_material = models.ForeignKey(SolMaterial, on_delete=models.CASCADE)
    materiales = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.materiales.nombre + " - " + str(self.cantidad)
    class Meta:
        verbose_name = "Solicitud de Material"
        verbose_name_plural = "Solicitudes de Material"