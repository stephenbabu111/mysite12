from django.contrib import admin
from .models import user

admin.site.register(user)
admin.site.site_header='ALC administrator'
# Register your models here.
