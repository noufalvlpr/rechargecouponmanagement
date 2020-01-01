from decimal import Decimal

import boto3
from decouple import config
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from rest_framework import views
from rest_framework.response import Response

from coupon.filters import BrandFilter, CouponFilter
from coupon.models import Coupon, Brand
from coupon.serializers import BrandSerializer
from botocore.exceptions import ClientError


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

    def get_queryset(self):
        coupon_filter = CouponFilter(self.request.GET, queryset=Coupon.objects.all())
        return coupon_filter.qs


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


class BrandListAPIView(views.APIView):
    def get(self, request):
        table_name = "brands"
        # Write to DynamoDB.
        table = boto3.resource(
            "dynamodb",
            region_name=config("AWS_REGION_NAME"),
            aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
        ).Table(table_name)
        response = table.scan()

        print(response["Items"])
        results = BrandSerializer(response["Items"], many=True).data
        return Response(results)


class BrandDetailAPIView(views.APIView):
    def get(self, request, pk):
        table_name = "brands"
        # Write to DynamoDB.
        table = boto3.resource(
            "dynamodb",
            region_name=config("AWS_REGION_NAME"),
            aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
        ).Table(table_name)
        try:
            response = table.get_item(Key={"id": pk})
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            item = response["Item"]
            return Response(BrandSerializer(item).data)
