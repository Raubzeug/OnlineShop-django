from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    type = models.ForeignKey(Category, on_delete=True)

    def __str__(self):
        return f'{self.type}: {self.title}'

    def get_absolute_url(self):
          return reverse('indexpage:product_page', args=[self.id])
