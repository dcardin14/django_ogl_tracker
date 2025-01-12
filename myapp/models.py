from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class OGL(models.Model):
    docNo = models.CharField(max_length=20)
    effDate = models.DateField()
    recDate = models.DateField()
    lessor = models.CharField(max_length=255)
    lessee = models.CharField(max_length=255)
    legal_desc = models.CharField(max_length=255, null=True, blank=True)
    term_in_years = models.DecimalField(max_digits=5, decimal_places=2)
    royalty = models.DecimalField(max_digits=6, decimal_places=6)

    def __str__(self):
        return self.docNo

class MineralTract(models.Model):
    township = models.CharField(max_length=5)
    range = models.CharField(max_length=5)
    section = models.IntegerField()
    desc = models.CharField(max_length=255, null=True, blank=True)
    gross = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    net = models.DecimalField(max_digits=5, decimal_places=2)
    ogl = models.ForeignKey(OGL, on_delete=models.CASCADE, related_name='mineral_tracts')

    def __int__(self):
        return self.section 
    