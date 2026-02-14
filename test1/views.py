from django.core.serializers import serialize
from django.shortcuts import render

from rest_framework.response import Response

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




