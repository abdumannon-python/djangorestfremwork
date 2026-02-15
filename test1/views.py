from django.core.serializers import serialize
from django.shortcuts import render
from pydantic.v1 import ValidationError

from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view
from .serializers import ProductSerialiser

@api_view(['GET'])
def get_info(request):
    data={
        'success':True,
        'message':'Hammasi joyida'
    }
    return Response(data)

@api_view(['POST'])
def create_product(request):
    serializer=ProductSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            'success': True,
            'message': 'product saqlandi',
            'data':serializer.data
        }

        return Response(data)
    raise ValidationError(serializer.errors)

@api_view(['GET'])
def list_product(request):
    product=Product.objects.all().order_by('-id')
    serializer=ProductSerialiser(product,many=True)
    data = {
        'success': True,
        'message': 'productlar',
        'data':serializer.data
    }
    return Response(data)


