from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_('Categories'), max_length=100)

    def __str__(self):
        return self.name
