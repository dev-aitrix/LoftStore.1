from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',)
    search_fields = ('email',)
    list_filter = ('first_name',)
    empty_value_display = '-пусто-'