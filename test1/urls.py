from django.urls import path

from test1.views import get_info,create_product,list_product

urlpatterns=[
    path('get_info/',get_info),
    path('create_p/',create_product),
    path('list/',list_product),

]