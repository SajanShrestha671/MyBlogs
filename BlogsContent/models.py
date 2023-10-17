from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
# Create your models here.
# category model
class category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.title}"
        
    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

# post model
class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True)
    url = models.CharField(max_length=100)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))
    
#project model
class project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=500, null=True)
    github = models.CharField(max_length=200, null=True)