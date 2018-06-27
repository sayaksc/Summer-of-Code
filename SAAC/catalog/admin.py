from django.contrib import admin

from .models import Batch, Student

# admin.site.register(Batch)
# admin.site.register(Student)
# admin.site.register(Programme)
# admin.site.register(StudentInstance)

class BatchAdmin(admin.ModelAdmin):
    list_display = ['year']

admin.site.register(Batch, BatchAdmin)


# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'branch', 'email', 'year')
    pass
admin.site.register(Student, StudentAdmin)
