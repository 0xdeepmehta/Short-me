from django.db import models
from .generator import generate

 
class Url(models.Model):
    url_id = models.CharField(max_length=50, default=generate(), unique=True)
    url = models.URLField()
    def __str__(self):
        return self.url + " -> " + self.url_id
