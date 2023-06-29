from django_filters import rest_framework as filters, FilterSet, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at']