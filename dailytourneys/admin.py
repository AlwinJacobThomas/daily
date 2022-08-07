from django.contrib import admin
from .models import BGMI
from .models import NewUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(BGMI)

class UserAdminConfig(UserAdmin):
  search_fields = ('email','username','first_name','orgname')
  list_filter = ('email','username','first_name','orgname','is_active','is_staff')
  ordering = ('-start_date',)
  list_display = ('email','username','first_name','orgname','is_active','is_staff')
  fieldsets = (
    (None, {'fields':('email','username','first_name','orgname',)}),('Permissions',{'fields':('is_staff','is_active')}),
    ('Personal',{'fields':('about',)}),
  )
  add_fieldsets = (
    (None, {
      'classes':('wide',),
      'fields':('email','username','first_name','password1','password2','is_active','is_staff')}
    ),
  )

admin.site.register(NewUser,UserAdminConfig)


