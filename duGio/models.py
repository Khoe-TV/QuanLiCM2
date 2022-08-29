from django.db import models

class duGioTable(models.Model):
    hoTen = models.CharField(max_length=255)
    toCM = models.CharField(max_length=50)
    ngayDu = models.CharField(max_length=20)
    phuChu = models.CharField(max_length=255)

class KHDGTG_Table(models.Model):
    hoTen = models.CharField(max_length=255)
    toCM = models.CharField(max_length=50)
    ngayDay = models.CharField(max_length=20)
    tenBai = models.CharField(max_length=255)
    lop = models.CharField(max_length=5)
    luotDu = models.CharField(max_length=2)
    loai = models.CharField(max_length=5)
    xepLoai = models.CharField(max_length=10)
    phuChu = models.CharField(max_length=255)