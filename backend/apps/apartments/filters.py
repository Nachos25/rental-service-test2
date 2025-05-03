from django_filters import rest_framework as filters
from .models import Apartment


class ApartmentFilter(filters.FilterSet):
    price_min = filters.NumberFilter(
        field_name="price", 
        lookup_expr='gte'
    )
    price_max = filters.NumberFilter(
        field_name="price", 
        lookup_expr='lte'
    )
    rooms = filters.NumberFilter(
        field_name="number_of_rooms", 
        lookup_expr='exact'
    )
    available = filters.BooleanFilter(field_name="availability")
    search = filters.CharFilter(method='search_filter')

    def search_filter(self, queryset, name, value):
        return queryset.filter(name__icontains=value) | queryset.filter(
            description__icontains=value
        )

    class Meta:
        model = Apartment
        fields = ['price_min', 'price_max', 'rooms', 'available', 'search'] 