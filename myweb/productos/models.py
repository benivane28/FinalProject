from django.db import models


# Create your models here.

class ServicioProd(models.Model):
    nombre= models.CharField(max_length=60)

    class Meta:
        verbose_name='servicioProd'
        verbose_name_plural='serviciosProd'
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=70)
    servicio= models.ForeignKey(ServicioProd,on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='productos',null=True,blank=True)
    precio= models.FloatField()
    disponibilidad= models.BooleanField(default=True)

    class META:
        verbose_name='producto'
        verbose_name_plural='productos'


