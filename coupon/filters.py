import django_filters

from coupon.models import Brand


class BrandFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Brand
        fields = ["name"]
