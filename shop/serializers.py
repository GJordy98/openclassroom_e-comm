from rest_framework.serializers import ModelSerializer

from .models import Category, Product, Article

from rest_framework import serializers





# class ProductSerializer(serializers.ModelSerializer):

#     articles = serializers.SerializerMethodField()
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'category', 'date_created', 'date_updated', 'articles']

#     def get_articles(self, instance):
#         queryset = instance.articles.filter(active=True)
#         serializer = ArticleSerializer(queryset, many=True)
#         return serializer.data
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ['id', 'name', 'category', 'date_created', 'date_updated', 'ecoscore']

class ProductDetailSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'articles', 'ecoscore']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data



class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'date_created', 'date_updated', 'price', 'product']

        def validate_price(self, value):
            if value < 1:
                raise serializers.ValidationError("Price must be greater than 1")
            return value
        
        def validate_product(self, value):
            if value.active is False:
                raise serializers.ValidationError("Product is inactive")
            return value

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated']
    

class CategoryDetailSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name'] 
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']
    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductDetailSerializer(queryset, many=True)

        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated', 'description']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("This category already exists")
        return value
    
    def validate(self, data):
        if data['name'] not in data['description']:
            raise serializers.ValidationError('The name should be included in the description')
        return data