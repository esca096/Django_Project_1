from .models import Product

from .serializer import ProductSerializer
from rest_framework import mixins, viewsets

class AppsViewset(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class AppsListRetriveviewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer