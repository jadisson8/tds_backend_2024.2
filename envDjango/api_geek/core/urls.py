from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from core import views


router = DefaultRouter()
router.register(r'vendas', views.VendaCRUD, basename='venda')
router.register(r'clientes', views.ClienteCRUD, basename='cliente')
router.register(r'produtos', views.ProdutoCRUD, basename='produto')
router.register(r'categorias', views.CategoriaCRUD, basename='categoria')
router.register(r'franquias', views.FranquiaCRUD, basename='franquia')
router.register(r'registros', views.RegistroCRUD, basename='registro')

venda_router = routers.NestedDefaultRouter(router, r'vendas', lookup='venda')
venda_router.register(r'registros', views.RegistroCRUD,
                      basename='venda-registros')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(venda_router.urls)),
]
