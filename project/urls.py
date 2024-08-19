from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.views import CategoryViewset, ProductViewSet, articleViewSet, AdminCategoryViewset, AdminArticlesViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')

router.register('products', ProductViewSet, basename='products')

router.register('articles', articleViewSet, basename='articles')

router.register('admin/category', AdminCategoryViewset, basename='admin-category')

router.register('admin/articles', AdminArticlesViewset, basename='admin-articles')

#from shop.views import CategoryView, ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/',  TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    





    # path('api/category/', CategoryView.as_view()),
    # path('api/products/',ProductView.as_view()),
]
