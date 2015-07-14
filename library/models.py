from django.conf import settings
from django.db import models

# Create your models here.

class Book(models.Model):
    # ID (automatic)
    # Title
    title = models.CharField(max_length=50)
    # Subtitle
    subtitle = models.CharField(max_length=70)
    # Author
    author = models.CharField(max_length=50)
    # description
    description = models.TextField()
    # keywords
    keywords = models.TextField()
    # ISBN
    isbn = models.CharField(max_length=13)
    # DDN
    ddn = models.CharField(max_length=10)
    # LCN
    lcn = models.CharField(max_length=10)
    


class Transaction(models.Model):
    # should include user, book, checked_out_date, due_date, refreshes_remaining, fees_assessed, fees_charged
    patron = models.ForeignKey(settings.AUTH_USER_MODEL)
    book = models.ForeignKey(Book)
    checkout_date = models.DateTimeField('Checkout Date')
    due_date = models.DateTimeField('Due Date')
    refreshes_remaining = models.IntegerField(default=0)
    fees_assessed = models.DecimalField(max_digits=5, decimal_places=2)
    fees_charged = models.DecimalField(max_digits=5, decimal_places=2)
