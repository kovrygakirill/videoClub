from django.contrib import admin
from .models import Category, Movie, UserLikeDislike, Comments


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie)
admin.site.register(UserLikeDislike)
admin.site.register(Comments)
