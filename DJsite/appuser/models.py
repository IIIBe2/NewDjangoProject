from django.db import models
from django.contrib.auth.models import User
from appsite.models import Product

class UserCustomPermission(models.Model):

    name =  models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    OpenProduct = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Доступ к продуктам'
        verbose_name_plural = 'Доступ к продуктам'

    def __exit__(self):
        return self.name