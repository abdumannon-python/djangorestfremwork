from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import Productserializers
from .models import Product
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializers

class ProductListView(APIView):

    def get(self,request):
        product=Product.objects.all()
        serializer=Productserializers(product,many=True)
        data={
            'status':status.HTTP_200_OK,
            'message':'Products',
            'data':serializer.data
        }
        return Response(data)


class ProductCreateView(APIView):
    def post(self,request):
        serializer=Productserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                'status':status.HTTP_201_CREATED,
                'message':'Product yaratildi',
                'data':serializer.data
            }

            return Response(data)

        data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Error',
            'data': serializer.data
        }
        return Response(data)

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = Productserializers

#
# class ProductUpdateView(UpdateAPIView):
#     def put(self, request, pk):
#         product = Product.objects.filter(pk=pk).first()
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'Product update',
#             "data": serializer.data
#         }
#
#         return Response(data)
#
#     def patch(self, request, pk):
#         product = Product.objects.filter(pk=pk).first()
#         serializer = ProductSerializer(product, request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'Product update',
#             "data": serializer.data
#         }
#
#         return Response(data)

# @api_view(['GET', ])
# def get_info(request):
#     data = {
#         'success': True,
#         "message": 'Hammasi joyida'
#     }
#     return Response(data)


# @api_view(['POST', ])
# def create_product(request):
#     serializer = ProductSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()

#         data = {
#             "success": True,
#             "message": "Product yaratildi",
#             "data": serializer.data
#         }
#         return Response(data)
#     raise ValidationError(serializer.errors)

# @api_view(['GET', ])
# def list_product(request):
#     products = Product.objects.all()[::-1]
#     if len(products) == 0:
#         raise ValidationError('Malumot yoq')
#     serializer = ProductSerializer(products, many=True)

#     data = {
#         "success": True,
#         "message": "Products",
#         "data": serializer.data
#     }
#     return Response(data)


# @api_view(['GET', ])
# def detail_product(request, pk):
#     product = Product.objects.filter(pk=pk).first()
#     if product is None:
#         raise ValidationError('Malumot topilmadi')
#     serializer = ProductSerializer(product)


