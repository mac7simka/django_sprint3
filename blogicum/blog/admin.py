from django.contrib import admin

from .models import Post, Category, Location


admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title', 'description', 'slug', 'created_at',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date', 'created_at', 'is_published',
                    'author', 'location', 'category',)
    list_editable = ('is_published', 'category',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
