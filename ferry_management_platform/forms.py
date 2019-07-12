from django import forms

CATEGORY = [("subject1", "科目一"), ("subject4", "科目四")]


class driving_exam_questions(forms.Form):  # 驾考真题批量维护
    file = forms.FileField(max_length=120)
    # subject_category = forms.ModelChoiceField(queryset=CATEGORY, empty_label='请选择分类')

