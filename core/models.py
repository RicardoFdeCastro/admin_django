from django.db import models

# Create your models here.
class categoria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name