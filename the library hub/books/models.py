from django.db import models
from django.utils.translation import gettext_lazy as _

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    class BookStatus(models.TextChoices):
        AVAILABLE = 'AV', _('Available')
        CHECKED_OUT = 'CO', _('Checked Out')
        RESERVED = 'RS', _('Reserved')
        LOST = 'LT', _('Lost')

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=255, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    edition = models.CharField(max_length=50, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    keywords = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=BookStatus.choices,
        default=BookStatus.AVAILABLE
    )
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"
