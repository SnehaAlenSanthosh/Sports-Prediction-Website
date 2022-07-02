from django.contrib import admin
from .models import Data

admin.site.site_header = 'Sports Prediction'
# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'height', 'sex', 'predictions')


admin.site.register(Data, DataAdmin)