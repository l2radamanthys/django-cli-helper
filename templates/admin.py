from django.contrib import admin
from %app%.models.%nombre_archivo% import %modelo%


class %modelo%Admin(admin.ModelAdmin):
    model = %modelo%
    list_display = (
        'id',
        'nombre',
    )

