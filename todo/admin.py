from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title',
                    # 'created_at', 
                    # 'description',
                    # 'due_date',
                    'author',
                    ]
    search_fields = ['title']
    # list_filter = ('status', 'category')
    # list_per_page = 10

admin.site.register(Todo, TodoAdmin)