from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Apartment(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    number_of_rooms = models.PositiveIntegerField()
    square = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='apartments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
