from django.db import models

# Create your models here.
class Sede(models.Model):
    """Django data model Sede"""
    sede = models.CharField(max_length=100,unique=True,error_messages={'unique':'Ya existe un registro con este nombre'})

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return '%s'%(self.sede)
