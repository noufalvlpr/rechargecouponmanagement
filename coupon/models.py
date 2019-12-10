import random
import string

from django.db import models, IntegrityError


class Brand(models.Model):
    name = models.CharField(max_length=20)
    code_length = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class CouponManager(models.Manager):
    def create_coupon(self, value, brand):
        coupon = self.create(
            value=value, code=Coupon.generate_code(brand.code_length), brand=brand
        )
        try:
            coupon.save()
        except IntegrityError:
            # Try again with other code
            coupon = Coupon.objects.create_coupon(value, brand)

        return coupon


class Coupon(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="coupons")
    code = models.CharField(max_length=100)
    value = models.PositiveIntegerField()

    objects = CouponManager()

    @classmethod
    def generate_code(cls, code_length):
        code = "".join(
            random.choice(string.ascii_letters + string.digits)
            for i in range(code_length)
        )
        return code
