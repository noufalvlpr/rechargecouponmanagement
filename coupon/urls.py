from django.urls import path
from coupon.views import CouponListView

urlpatterns = [
    path('', CouponListView.as_view(), name='coupon-list'),
]
