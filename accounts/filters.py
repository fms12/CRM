import django_filters 
# this helps to filter the out all products ................

from django_filters import DateFilter
from django_filters.filters import CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    # it's give the date filter column for the searching 
    start_date = DateFilter(field_name='date_created',lookup_expr='gte')
    end_date = DateFilter(field_name='date_created',lookup_expr='lte')
    note = CharFilter (field_name='note',lookup_expr = 'icontains')

    class Meta:
        model = Order
        fields ='__all__'
        exclude = ['customer','date_created','tags']
