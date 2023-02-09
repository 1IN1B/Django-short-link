from django.contrib import admin
from testapp.models import URL
# Register your models here.
class URLADMIN(admin.ModelAdmin):
    list_display = ['url','hidden_url']

admin.site.register(URL,URLADMIN)