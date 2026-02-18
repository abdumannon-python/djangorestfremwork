from django.urls import path,include
from  rest_framework.routers import DefaultRouter
from .views import ProductViewSet,ProductListView,ProductCreateView,ProductDetailView
router=DefaultRouter()
router.register('products',ProductViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('productlist/',ProductListView.as_view(),name='product-list'),
    path('create/',ProductCreateView.as_view(), name='create'),
    path('update-delete/<int:pk>/',ProductDetailView.as_view(),name='detail'),
]
