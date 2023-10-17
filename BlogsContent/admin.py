from django.contrib import admin
from .models import category, post, project

# to display category in the admin panel in the database form
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('cat_id','title', 'url','add_date', 'image_tag')
    search_fields = ('title','add_date')
    prepopulated_fields = {"slug": ('title',)}

# to display post in the admin panel in the database form
class postAdmin (admin.ModelAdmin):
    list_display = ('post_id','title', 'content','url','cat', 'image_tag','date')
    search_fields = ('title',)
    list_filter =('cat',)


# to display project in the admin panel in the database form
class ProjectAdmin (admin.ModelAdmin):
    list_display =('project_id','title','content', 'link','github')

    
# Register your models here.
admin.site.register(category, CategoryAdmin,)
 
admin.site.register(post, postAdmin)

admin.site.register(project, ProjectAdmin)