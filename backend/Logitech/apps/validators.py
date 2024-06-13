from .models import Product
from rest_framework import serializers


def validate_product_name(value):
        qs = Product.objects.filter(name__iexact=value)
        if qs.exists():
           raise serializers.ValidationError(f"le produict {value} exist deja")
        return value