from django.db import models

# Create your models here.


class Insurance(models.Model):
    title = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=100, null=True)
    provider = models.ForeignKey(
        "Provider", null=True, on_delete=models.PROTECT, related_name='provider')
    image = models.CharField(max_length=200, null=True)
    disclosure = models.CharField(max_length=30, null=True)
    execlusive = models.CharField(max_length=20, null=True)
    badge_label = models.CharField(max_length=20, null=True)
    badge_primary = models.CharField(max_length=20, null=True)
    snippet = models.TextField(null=True)
    snippet_img = models.CharField(max_length=200, null=True)
    keyfeatures = models.TextField(null=True)
    household = models.TextField(null=True)
    legal = models.TextField(null=True)
    accident = models.TextField(null=True)
    plan = models.TextField(null=True)

    def __str__(self):
        return self.title


class InsuranceUsp(models.Model):
    dd = models.CharField(max_length=30)
    dt = models.CharField(max_length=200)
    card = models.ForeignKey("Insurance", related_name='insurance_usp', on_delete=models.CASCADE)


class Provider(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=100, null=True)
