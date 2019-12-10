from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from coupon.models import Coupon, Brand


class BrandListView(ListView):
    model = Brand


class BrandCreateView(CreateView):
    model = Brand
    fields = ["name", "code_length"]
    success_url = "/brands/"


class CouponListView(ListView):
    model = Coupon
