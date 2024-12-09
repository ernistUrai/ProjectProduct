from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category, Product, Cart,  Order    


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = "__all__"
        

        
class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer
    
    class Meta:
        model = Order
        fields = "__all__"
        read_oniy_dields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username',  'email', 'password', 'password2')
        
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()      
        return user 