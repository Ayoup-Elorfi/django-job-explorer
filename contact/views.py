from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings


def contact_page(request):
    contact_info = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
    return render(request, 'contact/contact.html', {'contact_info': contact_info})
