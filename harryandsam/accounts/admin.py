from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Accounts

class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'number','email','address','last_login','is_admin','is_staff')
    search_fields = ('first_name', 'last_name', 'username','email')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Accounts, AccountAdmin)

