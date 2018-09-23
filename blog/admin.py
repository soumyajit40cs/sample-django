from django.contrib import admin
from .models import Post, Comment, Contact, Category, Subcategory
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date',)
    search_fields = ['title']
    ordering = ['-created_date']
    #list_filter = ['pub_date']
    #date_hierarchy = 'pub_date'


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Subcategory)
