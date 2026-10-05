from django import template
from ..models import Product
register = template.Library()

@register.simple_tag
def hello():
    return "alirezaaaaaaaaaaa"

@register.simple_tag(name='count')
def product_total():
    products = Product.objects.count()
    return products

@register.simple_tag(name='NameCount')
def product_total():
    products = Product.objects.all()
    return products

@register.inclusion_tag('store/inclusion.html')
def most_product():
    mp = Product.objects.all().order_by('name')
    return {'mp':mp}
