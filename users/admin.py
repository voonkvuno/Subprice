from django.contrib import admin
from django.utils.html import format_html
from users.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "fullname", "phone", "is_active", "is_admin", "get_picture"]
    search_fields = ["email", "fullname", "phone", "is_active"]
    
    @admin.display(description="프로필 사진")
    def get_picture(self, obj):
        if obj.picture:
            return format_html(f'<img src="{obj.picture.url}" alt="프로필 사진" style="width:30px; height:20px;">')
        else:
            return format_html(f'<img src="/static/img/profile.png" alt="프로필 사진" style="width:20px; height:20px;">')