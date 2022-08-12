from django.urls import path
from . import views

app_name = 'almacen'

urlpatterns = [
    path('', views.index, name='index'),
    path('sol_material', views.sol_material, name='sol_material'),
    path('form_sol_mat_sended', views.form_sol_mat_sended, name='form_sol_mat_sended'),
]