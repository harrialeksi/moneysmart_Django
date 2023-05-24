from django.db import models

# Create your models here.


class Card(models.Model):
    title = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=100, null=True)
    provider = models.ForeignKey(
        "Provider", null=True, on_delete=models.PROTECT, related_name='provider')
    association = models.ForeignKey(
        "Association", null=True, on_delete=models.PROTECT, related_name='association')
    image = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class CardDetail(models.Model):
    disclosure = models.CharField(max_length=30, null=True)
    execlusive = models.CharField(max_length=20, null=True)
    badge_label = models.CharField(max_length=20, null=True)
    badge_primary = models.CharField(max_length=20, null=True)
    snippet = models.TextField(null=True)
    snippet_img = models.CharField(max_length=200, null=True)
    card = models.ForeignKey("Card", related_name='card_details', on_delete=models.CASCADE)


class CardUsp(models.Model):
    dd = models.CharField(max_length=30)
    dt = models.CharField(max_length=200)
    card = models.ForeignKey("Card", related_name='card_usp', on_delete=models.CASCADE)


class Provider(models.Model):
    name = models.CharField(max_length=50)


class Association(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=100, null=True)
