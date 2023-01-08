from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class AddReviewForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Company'].empty_label = "Клиника не выбрана"

    class Meta:
        model = Reviews
        # fields = '__all__'  # список ВСЕХ полей формы
        fields = ['name', 'description', 'Company', 'stars', 'email']
        # виджеты с классами для полей
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_settings input'}),
            'description': forms.Textarea(attrs={'class': 'form_settings textarea', 'cols': 70, 'rows': 12}),
        }

    def clean_name(self):
        """
        Валидатор формы
        """
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return name


class FeedBackForm(forms.Form):
    captcha = CaptchaField()
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': "Ваше имя"
        })
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': "Ваша почта"
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': "Тема"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control md-textarea',
            'id': 'message',
            'rows': 2,
            'placeholder': "Ваше сообщение"
        })
    )


# class SearchCompanyForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         label='Название',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'name': 'name',
#             'label': 'label',
#             'placeholder': 'Найти'
#         })
#     )

class SearchCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']
        # виджеты с классами для полей
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_settings input', 'label_tag': 'Найти', 'placeholder': 'Найти'}),
        }

