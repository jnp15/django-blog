from django.contrib import admin
from django import forms
from polling.models import Poll
from blogging.models import Post, Category

'''
class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
'''

class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)


