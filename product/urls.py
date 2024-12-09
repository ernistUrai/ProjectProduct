from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product-list')
router.register(r'categories', CategoryViewSet, basename='category-list')
router.register(r'cart', CartViewSet, basename='cart-list')
router.register(r'orders', OrderViewSet, basename='orders-list')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('token/login/', TokenObtainPairView.as_view(), name='token-login'),
    path('token/login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
