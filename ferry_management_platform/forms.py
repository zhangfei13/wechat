from django import forms


class driving_exam_questions(forms.Form):  # 驾考真题批量维护
    file = forms.FileField(max_length=120)

