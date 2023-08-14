import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    #PRDName = django_filters.CharFilter(lookup_expr='icontains')
    #PRDDesc = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['PRDBrand','PRDImage','PRDPrice','PRDDiscountPrice','PRDCost','PRDCreated','PRDSLug','']
