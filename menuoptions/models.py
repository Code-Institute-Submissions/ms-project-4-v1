from django.db import models

# Create your models here.


class Category(models.Model):
    """ Category model """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ String method """
        return self.name

    def get_friendly_name(self):
        """ Model method to return friendly name """
        return self.friendly_name


