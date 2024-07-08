import os
import sys
import time
import django
from email.mime.image import MIMEImage
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


sys.path.append('/Users/alherdom/Library/Mobile Documents/com~apple~CloudDocs/Repos/pmo_junior')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pmo_junior.settings')
django.setup()


def send_report_email(mail, download_url):
    html_content = render_to_string(
        'report_email.html',
        {'download_url': download_url},
    )
    text_content = strip_tags(html_content)

    subject = 'Reporte diario de ventas'
    from_email = 'alehdezdguez@gmail.com'
    to_email = mail
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


while True:
    send_report_email('alherdom@outlook.com', 'http://localhost:8000/sales/date/2024-01-01/')
    time.sleep(60)
