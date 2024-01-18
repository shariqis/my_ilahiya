from django.contrib import admin
from Home.models import Employee
# Register your models here.


class EployeeAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')



admin.site.register(Employee,EployeeAdmin)
