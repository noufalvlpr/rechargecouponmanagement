from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView

from coupon.filters import BrandFilter
from coupon.models import Coupon, Brand


class BrandListView(ListView):
    model = Brand

    def get_queryset(self):
        brand_filter = BrandFilter(self.request.GET, queryset=Brand.objects.all())
        return brand_filter.qs


class BrandCreateView(CreateView):
    model = Brand
    fields = ["name", "code_length"]
    success_url = "/brands/"


class CouponListView(ListView):
    model = Coupon


class CouponCreateView(CreateView):
    model = Coupon
    fields = ["brand", "value"]
    success_url = "/coupons/"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = Coupon.objects.create_coupon(
            form.cleaned_data["value"], form.cleaned_data["brand"]
        )
        return HttpResponseRedirect(self.get_success_url())
