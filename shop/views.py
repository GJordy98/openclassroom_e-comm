from rest_framework.views import APIView
#from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import Category, Product, Article
from rest_framework.response import Response
from shop.serializers import CategoryDetailSerializer, ProductListSerializer, ArticleSerializer, CategoryListSerializer, ProductDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from shop.permissions import IsAdminAuthenticated, Partener


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
             return self.detail_serializer_class
        return super().get_serializer_class()

#class CategoryViewSet(ModelViewSet):
class CategoryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)
    
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
         self.get_object().disable()
         return Response()
    
    # def get_serializer_class(self):
    #      if self.action == 'retrieve':
    #           return self.detail_serializer_class
    #      return super().get_serializer_class()

class ProductViewSet(MultipleSerializerMixin,ReadOnlyModelViewSet):

    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
         queryset = Product.objects.filter(active=True)
         Category_id = self.request.GET.get('category_id')
         return queryset
    
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
         self.get_object().disable()
         return Response()
    
    


class articleViewSet(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):

        queryset = Article.objects.filter(active=True)

        product_id = self.request.GET.get('product_id')
        if product_id:
              queryset = queryset.filter(product_id=product_id)
        return queryset



class AdminCategoryViewset(MultipleSerializerMixin, ModelViewSet):
     
     serializer_class = CategoryListSerializer
     detail_serializer_class = CategoryDetailSerializer

     permission_classes = [IsAdminAuthenticated]   #[Partener]
     def get_queryset(self):
          return Category.objects.all()
     

class AdminArticlesViewset(MultipleSerializerMixin, ModelViewSet):
     serializer_class = ArticleSerializer
     
     def get_queryset(self):
          return Article.objects.all()



# class CategoryView(APIView):
#     def get(self, *args, **kwargs):
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset, many=True)
#         return Response(serializer.data)
    
# class ProductView(APIView):
#     def get(self, *args, **kwargs):
#         queryset = Product.objects.all()
        # serializer = ProductSerializer(queryset, many=True)
        # return Response(serializer.data)

