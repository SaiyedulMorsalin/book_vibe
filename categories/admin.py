from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display =['id','category','slug']
    prepopulated_fields = {'slug':('category',)}
    

admin.site.register(Category,CategoryAdmin)