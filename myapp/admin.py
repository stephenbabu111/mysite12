from django.contrib import admin
from .models import user,exam_halls

admin.site.register(user,)
admin.site.register(exam_halls)
admin.site.site_header='ALC administrator'
# Register your models here.
