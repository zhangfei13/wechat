from django.contrib import admin
from ferry_management_platform.models import v_user, enum_info, entry_special_info

# Register your models here.


class v_userAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'wechat_no', 'id_type', 'id_no', 'name', 'phone', 'user_level', 'status', 'self_proc_illegal', 'desc']
    search_fields = ['name']
    list_filter = ['status']

    # list_per_page设置每页显示多少条记录，默认是100条
    # list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-status',)

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    # list_editable = ['name', 'phone']

    # 设置哪些字段可以点击进入编辑界面
    # list_display_links = ('user_id', 'wechat_no')

    # 列表顶部，设置为False不在顶部显示，默认为True。
    # actions_on_top = True

    # 列表底部，设置为False不在底部显示，默认为False。
    # actions_on_bottom = False


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
