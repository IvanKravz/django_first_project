from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField(max_length=50)
    image = models.CharField()
    release_date = models.DateField(max_length=20)
    lte_exists = models.BooleanField(max_length=10)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
