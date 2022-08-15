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
    def __str__(self):
        return self.tecnico.nombre
    class Meta:
        verbose_name = "Solicitud de Material Por Tecnico"
        verbose_name_plural = "Solicitudes de Material Por Tecnico"
    

class SolMaterialChoises(models.Model):
    tecnico = models.ForeignKey(SolMaterial, on_delete=models.CASCADE)
    material = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Retorna el nombre del material, la cantidad y el técnico que solicitó'''
        return self.material.cod_seot + " - " + self.material.nombre + " - " + str(self.cantidad) + " - " + self.tecnico.tecnico.nombre
    class Meta:
        verbose_name = "Solicitud de Material"
        verbose_name_plural = "Solicitudes de Material"
