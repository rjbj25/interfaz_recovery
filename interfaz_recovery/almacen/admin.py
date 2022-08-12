from django.contrib import admin
from .models import Recurso, Tecnico, SolMaterial, SolMaterialChoises

class SolMaterialChoisesInline(admin.StackedInline):
    model = SolMaterialChoises
    extra = 3

class SolMaterialAdmin(admin.ModelAdmin):
    inlines = [SolMaterialChoisesInline]

# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tecnico)
admin.site.register(SolMaterial, SolMaterialAdmin)
