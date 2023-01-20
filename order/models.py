from django.db import models
from user.models import User


class Order(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='buyer_orders')
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='seller_orders')
    status = models.CharField(max_length=15, choices=[(
        'pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
