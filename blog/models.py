from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
