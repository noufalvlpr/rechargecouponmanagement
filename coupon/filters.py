import django_filters
from django.db.models import Q

from coupon.models import Brand, Coupon


class BrandFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Brand
        fields = ["name"]


class CouponFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method="my_custom_filter")

    class Meta:
        model = Coupon
        fields = ["q"]

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(code__icontains=value)
            | Q(brand__name__icontains=value)
            | Q(value__icontains=value)
        )
