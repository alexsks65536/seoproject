"""
# In settings.py
# Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'smolgu.bureau.website@gmail.com'
EMAIL_HOST_PASSWORD = 'bureausmolgu'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
"""


from django.core.mail import send_mail
from django.forms import ModelForm
from django.template import RequestContext


class ContactUsForm(ModelForm):
    class Meta:
        model = MailBox
        fields = ['subject', 'message', 'sender']


def contact_us(request):
    path_back = request.META.get('HTTP_REFERER', '/')

    if request.method == 'POST':  # If the form has been submitted...
        contact_form = ContactUsForm(request.POST)  # A form bound to the POST data
        if contact_form.is_valid():  # All validation rules pass
            subject = contact_form.cleaned_data['subject']
            sender = contact_form.cleaned_data['sender']
            message = 'Письмо было отправлено с сайта, адрес для ответа %s \r\n \r\n' % sender
            message += contact_form.cleaned_data['message']
            recipients = ['skymorr@yandex.ru']

            # Положим копию письма в базу на всякий случай
            MailBox.objects.create(subject=subject, sender=sender, message=message)

            # и отправим его
            try:
                send_mail(subject, message, sender, recipients, fail_silently=False)
            except:
                send_mail(subject, message, sender, recipients, fail_silently=False)

            return render_to_response('web_site/success.html', {'path_back': path_back},
                                      context_instance=RequestContext(request))

    return render_to_response('web_site/fail.html', context_instance=RequestContext(request))