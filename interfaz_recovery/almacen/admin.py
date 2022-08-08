from django.contrib import admin
from .models import Recurso, Tecnico, SolMaterial

# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tecnico)
admin.site.register(SolMaterial)
