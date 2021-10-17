from django.contrib import admin
from .models import Todo

# sajinisadanandpython
class TodoAdmin(admin.ModelAdmin):
    list = ('title','description','completed')
    
admin.site.register(Todo,TodoAdmin)