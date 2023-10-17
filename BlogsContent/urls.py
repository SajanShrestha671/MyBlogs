
from django.urls import path
from BlogsContent.views import index, blogs, projects, singleposts, about, categoryView

urlpatterns = [
    path('', index),
    path('blogs/', blogs),
    path('projects/', projects),
    path('about/', about),
    path('blogs/category/<str:cat_id>', categoryView),
    path('blogs/category/singlepost/<int:post_id>', singleposts)
]
