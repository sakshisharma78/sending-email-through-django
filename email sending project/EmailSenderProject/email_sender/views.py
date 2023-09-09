from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        recipients = request.POST['recipients']  # Comma or semicolon separated
        
        recipient_list = [recipient.strip() for recipient in recipients.split(';')]
        
        send_mail(subject, message, 'sakshisharma@gmail.com', recipient_list)
        return HttpResponse('Email sent successfully!')
    return render(request, 'send_emails.html')
