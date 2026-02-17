from django.urls import path,include
from  rest_framework.routers import DefaultRouter
from .views import ProductViewSet,ProductListView
router=DefaultRouter()
router.register('products',ProductViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('productlist/',ProductListView.as_view(),name='product-list')
]