from django.contrib import admin
from .models import Recurso, Tecnico, SolMaterial, SolMaterialChoises
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionMixin
from import_export import resources

class SolMaterialChoisesInline(admin.StackedInline):
    model = SolMaterialChoises
    extra = 0

class SolMaterialAdmin(admin.ModelAdmin):
    # Se muestran las solicitudes de material con sus choises
    inlines = [SolMaterialChoisesInline]
    list_display = ('pk', 'tecnico')
    list_filter = ('tecnico',)
    search_fields = ('tecnico',)


class SolMaterialChoisesResource(resources.ModelResource):
    class Meta:
        model = SolMaterialChoises
        fields = ('tecnico__tecnico__nombre', 'material__nombre', 'material__cod_seot', 'cantidad', 'fecha_hora')
        export_order = ('tecnico__tecnico__nombre', 'material__nombre', 'material__cod_seot', 'cantidad', 'fecha_hora')


class SolMaterialChoisesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('tecnico', 'material', 'cantidad', 'fecha_hora')
    list_filter = ('tecnico', 'material', 'cantidad', 'fecha_hora')
    resource_class = SolMaterialChoisesResource


# Register your models here.
admin.site.register(Recurso)
admin.site.register(Tecnico)
admin.site.register(SolMaterial, SolMaterialAdmin)
admin.site.register(SolMaterialChoises, SolMaterialChoisesAdmin)
