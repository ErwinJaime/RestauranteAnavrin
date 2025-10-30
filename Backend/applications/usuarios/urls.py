# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Ruta de prueba
    path('', views.saludo, name='saludo'),
    
    # ========== AUTENTICACIÓN ==========
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('google-login/', views.google_login, name='google_login'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/actualizar/', views.actualizar_perfil, name='actualizar_perfil'),
    
    # ========== PRODUCTOS ==========
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/actualizar/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
    # ========== PEDIDOS ==========
    path('pedidos/', views.listar_pedidos_usuario, name='listar_pedidos_usuario'),
    path('pedidos/todos/', views.listar_todos_pedidos, name='listar_todos_pedidos'),
    path('pedidos/<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/<int:pk>/actualizar/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/<int:pk>/estado/', views.cambiar_estado_pedido, name='cambiar_estado_pedido'),
    path('pedidos/<int:pk>/cancelar/', views.cancelar_pedido, name='cancelar_pedido'),
    
    # ========== RESEÑAS ==========
    path('productos/<int:producto_id>/resenas/', views.listar_resenas_producto, name='listar_resenas_producto'),
    path('resenas/', views.listar_resenas_usuario, name='listar_resenas_usuario'),
    path('resenas/todas/', views.listar_todas_resenas, name='listar_todas_resenas'),
    path('resenas/crear/', views.crear_resena, name='crear_resena'),
    path('resenas/<int:pk>/actualizar/', views.actualizar_resena, name='actualizar_resena'),
    path('resenas/<int:pk>/eliminar/', views.eliminar_resena, name='eliminar_resena'),
    path('resenas/<int:pk>/visibilidad/', views.cambiar_visibilidad_resena, name='cambiar_visibilidad_resena'),
]