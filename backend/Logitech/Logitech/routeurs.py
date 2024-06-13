from rest_framework.routers import DefaultRouter
from apps.viewset import AppsViewset, AppsListRetriveviewset

routeur = DefaultRouter()

routeur.register('product-b', AppsViewset, basename='product-a')

print(routeur.urls)
urlpatterns = routeur.urls