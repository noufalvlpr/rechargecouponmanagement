from django.urls import path
from coupon.views import CouponListView, CouponCreateView, BrandListView, BrandCreateView

urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('coupons/', CouponListView.as_view(), name='coupon-list'),
    path('coupons/create/', CouponCreateView.as_view(), name='coupon-create'),
]
