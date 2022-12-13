from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class ContactForm(forms.ModelForm):
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
