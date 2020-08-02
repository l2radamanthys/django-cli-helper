from django.contrib import admin
from series.models.series import Serie


class %modelo%Admin(admin.ModelAdmin):
    model = %modelo%
    list_display = (
        'nombre',
    )

