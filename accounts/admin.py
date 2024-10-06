from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')   # Propiedades que queremos que se muestren en el grid de la tabla de usuarios
    list_diaplay_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)    # Ordenamiento ascendente
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    

# Register your models here.
admin.site.register(Account, AccountAdmin)
