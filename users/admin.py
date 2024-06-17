from django.contrib import admin
from users.models import CustomUser

class AdminCustomUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')



admin.site.register(CustomUser, AdminCustomUser)

