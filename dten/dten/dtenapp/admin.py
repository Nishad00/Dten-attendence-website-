from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Person)
admin.site.register(Subject)
admin.site.register(Division)
admin.site.register(batch)
admin.site.register(Attend)