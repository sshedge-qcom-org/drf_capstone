from django.db import models

# Create your models here.

class Book(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        OUT_OF_STOCK = 'out_of_stock', 'Out Of Stock'
        DISCONTINUED = 'discontinued', 'Discontinued'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.title} by {self.author}"

