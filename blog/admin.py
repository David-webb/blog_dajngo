from django.contrib import admin

# Register your models here.
from blog import models as blog_models
admin.site.register(blog_models.Article)
