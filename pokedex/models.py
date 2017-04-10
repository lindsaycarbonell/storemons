from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    # author = models.ForeignKey('auth.User')
    dex_num = models.IntegerField(blank=True, null=True)
    species = models.CharField(max_length=200)
    type1 = models.CharField(max_length=200)
    type2 = models.CharField(max_length=200)
    added_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.species
