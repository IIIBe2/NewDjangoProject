from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Product(models.Model):

    author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.name
    


class Lesson(models.Model):
    productSet1 = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=300, db_index=True)
    secondsLesson = models.DurationField()

    class Meta:
        ordering = ('name', )
        verbose_name = 'Урок'
        verbose_name_plural = 'Урок'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name



class UserCustom(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    lessonID = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    TimeWatch = models.DurationField(blank=True, null=True)
    

    class Meta:
        ordering = ('name', )
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзер'

    def __exit__(self):
        return self.name