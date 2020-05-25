from django.db import models
from django.urls import reverse
# Create your models here.
class NhanVien(models.Model):
    name=models.CharField(max_length=100)
    adrress=models.CharField(max_length=255)
    email=models.EmailField()
    chucvu=models.CharField(max_length=100)
    tuoi=models.IntegerField()

    def __str__(self):
        return self.name

    def __get_absolute_url(self):
        return reverse('nhanvien_update',kwargs={'pk':self.pk})