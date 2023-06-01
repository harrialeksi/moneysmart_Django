from django.db import models

# Create your models here.


class Card(models.Model):
    title = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=100, null=True)
    provider = models.ForeignKey(
        "Provider", null=True, on_delete=models.PROTECT, related_name='provider')
    association = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    disclosure = models.CharField(max_length=30, null=True)
    execlusive = models.CharField(max_length=20, null=True)
    badge_label = models.CharField(max_length=20, null=True)
    badge_primary = models.CharField(max_length=20, null=True)
    snippet = models.TextField(null=True)
    snippet_img = models.CharField(max_length=200, null=True)
    url = models.TextField(max_length=200, null=True)
    promotion = models.TextField(null=True)
    keyfeatures = models.TextField(null=True)
    annualinterest = models.TextField(null=True)
    incomeequirement = models.TextField(null=True)
    cardassociation = models.TextField(null=True)
    wirelesspayment = models.TextField(null=True)

    def __str__(self):
        return self.title


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
    doc = models.TextField(null=True)
