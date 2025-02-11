from django.db import models
from books.models import Book
from members.models import Member
from django.utils import timezone

class BookLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.due_date:
            membership_type = self.member.membership_type
            self.due_date = timezone.now() + timezone.timedelta(days=membership_type.loan_duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} - {self.member.user.username}"
