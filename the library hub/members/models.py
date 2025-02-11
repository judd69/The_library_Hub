from django.db import models
from django.contrib.auth.models import User

class MembershipType(models.Model):
    name = models.CharField(max_length=100)
    max_books = models.IntegerField(default=3)
    loan_duration_days = models.IntegerField(default=14)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
