from django.db import models

# Create your models here.
class Knight(models.Model):
    """Features of a Knight
    """
    name = models.CharField(max_length=100, unique=True)
    of_the_round_table = models.BooleanField()
    dances_whenever_able = models.BooleanField()
    shrubberies = models.IntegerField(null=False)


class Group(models.Model):
    name = models.TextField(verbose_name="Name")
    facebook_page__id = models.CharField(max_length=255)
        
