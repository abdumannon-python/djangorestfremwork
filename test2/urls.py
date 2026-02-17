from django.urls import path,include
from  rest_framework.routers import DefaultRouter
from .views import ProductViewSet
router=DefaultRouter
router.register('Products',ProductViewSet.as_view)

urlpatterns=[
    path('',include(router.urls)),
]