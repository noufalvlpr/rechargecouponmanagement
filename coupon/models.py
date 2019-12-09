from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20)
    code_length = models.PositiveIntegerField()


class Coupon(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='coupons')
    code = models.CharField(max_length=100)
    value = models.PositiveIntegerField()