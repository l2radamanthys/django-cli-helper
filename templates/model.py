from django.db import models


class %modelo%(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        db_table = '%nombre_tabla%'
        verbose_name = "%modelo%"
        verbose_name_plural = "%nombre_plural%"

    def __str__(self):
        return self.nombre
