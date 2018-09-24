from django.contrib import admin
from .models import Post, Comment, Contact, Continent, Country
from django.utils import timezone
# Register your models here.




class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date','published_date',)
    search_fields = ['title']
    ordering = ['-created_date']
    actions = ['make_published',]
    #list_filter = ['pub_date']
    #date_hierarchy = 'pub_date'
    def make_published(modeladmin, request, queryset):
        for post in queryset:
            post.published_date = timezone.now()
            post.save()
    make_published.short_description = "Mark selected stories as published"


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Continent)
admin.site.register(Country)
