from django.contrib import admin
from .models import Post, UserNew, Comment_on_Post,Comment


# Register your models here.
class CommentReal(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if (obj and (obj.comment_user.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if (obj and (obj.comment_user.user == request.user)) or request.user.is_superuser:
            return True
        return False

admin.site.register(Comment,CommentReal)
class CommentAdmin(admin.TabularInline):
    model = Comment_on_Post
    extra = 0
    list_display = ("comment_description", "date_comment_created")

    def has_add_permission(self, request, obj = None):
        return True
    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if (obj and (obj.user.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj = None):
        if (obj and (obj.user.user == request.user)) or request.user.is_superuser:
            return True
        return False




class PostAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None) :
        if (obj and (obj.user.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj = None):
        if (obj and (obj.user.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True


    list_display = ("title", "description",)
    search_fields = ("title", "description",)
    list_filter = ("date_created",)
    inlines = [CommentAdmin, ]


admin.site.register(Post, PostAdmin)


class UserAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if (obj and (obj.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if (obj and (obj.user == request.user)) or request.user.is_superuser:
            return True
        return False




    list_display = ("name",)




admin.site.register(UserNew, UserAdmin)


