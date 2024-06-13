from rest_framework import serializers

from apps.models import Product




class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="apps-details", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()
    

class UserpublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    has_perms = serializers.BooleanField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ('username', 'id', 'has_perms', 'user_product')
    
    
    def get_user_product(self, obj):
        user = obj
        request = self.context.get('request')
        product = user.product_set.all()
        return ProductInlineSerializer(product, many=True, context={'request':request}).data
    