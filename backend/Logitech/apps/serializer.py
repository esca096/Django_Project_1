from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializer import UserpublicSerializer

from .models import Product
from .validators import validate_product_name


"""class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="apps-details", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()"""


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    #url = serializers.SerializerMethodField(read_only = True)
    """owner = UserProductInlineSerializer(source='user.product_set.all', many=True, read_only=True)"""
    url = serializers.HyperlinkedIdentityField(view_name="apps-details", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    owner = serializers.CharField(source='user', read_only=True)
    name = serializers.CharField(validators=[validate_product_name])
    #user_name = serializers.CharField(source="user", read_only=True)
    class Meta:
        model = Product
        fields = ('owner','email','url','pk','name', 'content', 'price', 'my_discount', 'public')
    
    
    """def get_owner(self, obj):
        return {'username':obj.user.username, 'id':obj.user.pk}"""
    
    
    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        print(email)
        print(validated_data)
        #return Product.objects.create(**validated_data)
        obj = super().create(validated_data)
        return obj
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        return super().update(instance, validated_data)
        
    """def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("apps-details", kwargs={'pk':obj.pk}, request=request)"""
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount