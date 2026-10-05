from django.contrib import admin

from .models import Department, ExchangeProgram, FacultyInfo, Program, Teacher

admin.site.register(Department)
admin.site.register(FacultyInfo)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(ExchangeProgram)
