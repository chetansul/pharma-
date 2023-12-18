from django.contrib import admin
from .models import drugs,zone,stability,result
# Register your models here.

admin.site.register(drugs)
admin.site.register(zone)
admin.site.register(stability)
admin.site.register(result)