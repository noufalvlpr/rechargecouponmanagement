from django.urls import path
from coupon.views import CouponListView, CouponCreateView, BrandListView, BrandCreateView, BrandListAPIView, \
    BrandDetailAPIView

urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('coupons/', CouponListView.as_view(), name='coupon-list'),
    path('coupons/create/', CouponCreateView.as_view(), name='coupon-create'),
    path('api/brands/', BrandListAPIView.as_view(), name='brand-list-api'),
    path('api/brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail-api'),
]
