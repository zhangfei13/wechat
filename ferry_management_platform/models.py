from django.db import models

# Create your models here.


class enum_info(models.Model):
    enum_no = models.IntegerField("枚举编号")
    enum_type = models.CharField("枚举类型", max_length=50, blank=True, null=True)
    enum_subtype = models.CharField("枚举二级类型", max_length=50, blank=True, null=True)
    enum_value = models.CharField("枚举值", max_length=120, blank=True, null=True)
    desc = models.CharField("描述", max_length=120, blank=True, null=True)

    class Meta:
        db_table = "enum_info"


class v_user(models.Model):
    user_id = models.BigAutoField("用户ID", primary_key=True)
    wechat_no = models.CharField("微信号", max_length=60, unique=True)
    id_type = models.IntegerField("证件类型")
    id_no = models.CharField("证件号码", max_length=30, blank=True, null=True)
    name = models.CharField("姓名", max_length=60, blank=True, null=True)
    phone = models.CharField("电话号码", max_length=20, blank=True, null=True)
    user_level = models.IntegerField("用户级别")
    status = models.CharField("用户状态", max_length=10, choices=[("on", "可用"), ("close", "不可用")])
    self_proc_illegal = models.CharField("用户状态", max_length=10, choices=[("on", "可用"), ("close", "不可用")])
    desc = models.TextField("描述", max_length=120)

    class Meta:
        db_table = "v_user"


class entry_special_info(models.Model):
    table_name = models.CharField("操作的表名", max_length=60, blank=True, null=True)
    opr_type = models.CharField("操作类型", max_length=10, blank=True, null=True)
    opr_name = models.CharField("操作名称", max_length=60, blank=True, null=True)

    class Meta:
        db_table = "entry_special_info"


