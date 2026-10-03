from django.urls import path
from . views import *

app_name = 'store'

urlpatterns = [
    path('', store_home, name='home'),
    path('products/', product_list, name='product_list'),
    path('test/', test , name='test'),
]   