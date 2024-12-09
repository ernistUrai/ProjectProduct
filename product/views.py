from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.contrib.auth import authenticate

# from .filters import ShoesFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Cart, Order
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, UserSerializer, OrderSerializer
from .filters import ProductFilter

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter
    


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        cart = self.get_object()  
        cart_serializer = self.get_serializer(cart)
        products = cart.product.all() 
        product_serializer = ProductSerializer(products, many=True)

        response_data = cart_serializer.data 
        response_data['products'] = product_serializer.data 
        return Response(response_data, status=status.HTTP_200_OK)

   

     
   
    
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(user=user)
        return Order.objects.none()
    
    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()  
        order_serializer = self.get_serializer(order)
        
        cart = order.cart  
        cart_serializer = CartSerializer(cart) 
       
        response_data = order_serializer.data  
        response_data['cart'] = cart_serializer.data  
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    
class RegisterApiView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  

        return Response({
            'username': user.username,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)
        
        
        
    
# class LoginApiView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
         
#         if user is not None:
#             token = Token.objects.get(user=user)
#             return Response({
#                 'username': user.username,
#                 'email': user.email,
#                 'token': token.key,
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 'massage': 'Неверный логин или пароль'
#             }, status=status.HTTP_401_UNAUTHORIZED)
            