from django.contrib import admin
from ferry_management_platform.models import v_user, enum_info, entry_special_info

# Register your models here.


class v_userAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'wechat_no', 'id_type', 'id_no', 'name', 'phone', 'user_level', 'status', 'self_proc_illegal', 'desc']
    search_fields = ['name']
    list_filter = ['status']


class enum_infoAdmin(admin.ModelAdmin):
    list_display = ['enum_no', 'enum_type', 'enum_subtype', 'enum_value', 'desc']
    search_fields = ['enum_type']
    list_filter = ['enum_type']


class entry_special_infoAdmin(admin.ModelAdmin):
    list_display = ['table_name', 'opr_type', 'opr_name']
    search_fields = ['table_name']
    list_filter = ['table_name']


admin.site.register(v_user, v_userAdmin)
admin.site.register(enum_info, enum_infoAdmin)
admin.site.register(entry_special_info, entry_special_infoAdmin)
