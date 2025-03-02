from django.contrib import admin
from About_us.models import Teacher
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id', 'tid', 'tname', 'emain')
admin.site.register(Teacher, TeacherAdmin)    