from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from apps.models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = "is_public"
    fields = [
        'user',
        'name',
        'content',
        'price',
        'public'
    ]
    tags = "get_tags_list"
    
    settings = {
        'searchableAttributes':['name', 'content'],
        'attributesForFaceting':['user', 'public']
    }