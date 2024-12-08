from django.urls import path
from inventario import views  # Esta línea estaba combinada con el siguiente import, lo cual es incorrecto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipos/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    path('equipos/exportar_pdf/<int:equipo_id>/', views.exportar_equipo_pdf, name='exportar_equipo_pdf'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
