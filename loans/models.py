from django.db import models

# Create your models here.


class Loan(models.Model):
    title = models.CharField(max_length=30, null=True)
    feature = models.ForeignKey(
        "Feature", null=True, on_delete=models.PROTECT, related_name='feature')
    bank = models.ForeignKey(
        "Bank", null=True, on_delete=models.PROTECT, related_name='bank')
    image = models.CharField(max_length=200, null=True)
    disclosure = models.CharField(max_length=30, null=True)
    execlusive = models.CharField(max_length=20, null=True)
    badge_label = models.CharField(max_length=20, null=True)
    badge_primary = models.CharField(max_length=20, null=True)
    snippet = models.TextField(null=True)
    snippet_img = models.CharField(max_length=200, null=True)
    promotion = models.TextField(null=True)
    keyfeatures = models.TextField(null=True)
    repayment = models.TextField(null=True)

    def __str__(self):
        return self.title


class LoanUsp(models.Model):
    dd = models.CharField(max_length=30)
    dt = models.CharField(max_length=200)
    card = models.ForeignKey("Loan", related_name='loan_usp', on_delete=models.CASCADE)


class Feature(models.Model):
    name = models.CharField(max_length=50)


class Bank(models.Model):
    name = models.CharField(max_length=50)

