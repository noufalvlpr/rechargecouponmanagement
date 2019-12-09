from django.views.generic import ListView
from coupon.models import Coupon


class CouponListView(ListView):
    model = Coupon
