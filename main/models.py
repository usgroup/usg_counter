from django.db import models
from django.utils import timezone


class Owner(models.Model):
    name = models.CharField("Ismi", max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Direktor"
        verbose_name_plural = "Direktorlar"


class Client(models.Model):
    name = models.CharField("Ismi", max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"


class Developer(models.Model):
    name = models.CharField("Ismi", max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Dasturchi"
        verbose_name_plural = "Dasturchilar"


class Payment(models.Model):
    comment = models.CharField("Izohi", max_length=550)
    type = models.IntegerField("Turi", choices=(
        (1, 'Kirim'),
        (2, 'Chiqim'),
    ))
    date = models.DateField("Sanasi", blank=True, null=True, default=timezone.now)
    amount_in_uzs = models.FloatField("Kirim (UZS)", blank=True, null=True)
    amount_in_usd = models.FloatField("Kirim (USD)", blank=True, null=True)
    amount_out_uzs = models.FloatField("Chiqim (UZS)", blank=True, null=True)
    amount_out_usd = models.FloatField("Chiqim (USD)", blank=True, null=True)

    owner = models.ForeignKey(Owner, verbose_name="Direktor", on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Client, verbose_name="Mijoz", on_delete=models.CASCADE, blank=True, null=True)
    dev = models.ForeignKey(Developer, verbose_name="Dasturchi", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name = "To'lov"
        verbose_name_plural = "To'lovlar"