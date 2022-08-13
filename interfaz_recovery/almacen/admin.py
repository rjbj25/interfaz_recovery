from django.contrib import admin
from .models import Recurso, Tecnico, SolMaterial, SolMaterialChoises

class SolMaterialChoisesInline(admin.StackedInline):
    model = SolMaterialChoises
    extra = 0

class SolMaterialAdmin(admin.ModelAdmin):
    # Se muestran las solicitudes de material con sus choises

    inlines = [SolMaterialChoisesInline]
    list_display = ('tecnico', 'fecha_hora')
    list_filter = ('tecnico', 'fecha_hora')
    search_fields = ('tecnico', 'fecha_hora')

    
class SolMaterialChoisesAdmin(admin.ModelAdmin):
    list_display = ('cod_material', 'materiales', 'cantidad')
    list_filter = ('cod_material', 'materiales', 'cantidad')

# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tecnico)
admin.site.register(SolMaterial, SolMaterialAdmin)
admin.site.register(SolMaterialChoises, SolMaterialChoisesAdmin)
