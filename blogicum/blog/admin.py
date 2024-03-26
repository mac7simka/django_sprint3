from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title', 'description', 'slug', 'created_at',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date', 'created_at', 'is_published',
                    'author', 'location', 'category',)
    list_editable = ('is_published', 'category',)


admin.site.register(Location)
