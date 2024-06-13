from .models import Product
from .serializer import ProductSerializer
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from api.mixims import StaffEditorPermissionsMixims, UserQuerySetAppsMixims
  
#concerne la view
class DetailAppsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
#concerne la create & List wiew
class CreateAppsView(StaffEditorPermissionsMixims,UserQuerySetAppsMixims, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content, user=self.request.user)
        
    
        
        
class UpdateAppsView(StaffEditorPermissionsMixims,UserQuerySetAppsMixims,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)
        

class DeleteAppsView(StaffEditorPermissionsMixims,UserQuerySetAppsMixims,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

"""
Concerne la creation de la liste mais peut etre utiliser au nieau update

class ListAppsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return super().get_queryset().filter(name__icontains='orange')"""


        
# c'est le mixage de tout les codes en dessus         
class AppsMixinsViews(generics.GenericAPIView,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin):
    
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)
    
    
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)  
    
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
