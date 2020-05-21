from django.db import models

 
class Url(models.Model):
    url_id = models.CharField(max_length=50, unique=True)
    url = models.URLField()
    def __str__(self):
        return self.url + " -> " + self.url_id
