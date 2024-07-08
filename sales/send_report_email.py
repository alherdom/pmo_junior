import os
import sys
import time
import datetime
import django
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

sys.path.append('/Users/alherdom/Library/Mobile Documents/com~apple~CloudDocs/Repos/pmo_junior')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pmo_junior.settings')
django.setup()


def send_report_email(mail, daily_url, monthly_url):
    html_content = render_to_string(
        'report_email.html',
        {'daily_url': daily_url, 'monthly_url': monthly_url},
    )
    text_content = strip_tags(html_content)

    subject = 'Reporte de ventas diario y acumulado mensual'
    from_email = 'alehdezdguez@gmail.com'
    to_email = mail
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def get_daily_url():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    return f'http://localhost:8000/sales/date/{yesterday.strftime("%Y-%m-%d")}/'


def get_monthly_url():
    current_date = datetime.datetime.now()
    return f'http://localhost:8000/sales/month/{current_date.strftime("%Y")}/{current_date.strftime("%m")}/'


while True:
    current_time = datetime.datetime.now()
    send_hour = 8

    if current_time.hour == send_hour and current_time.minute == 0:
        daily_url = get_daily_url()
        monthly_url = get_monthly_url()
        send_report_email('alherdom@outlook.com', daily_url, monthly_url)
        time.sleep(60 * 60 * 24)
    else:
        time.sleep(60)


# while True:
#     daily_url = get_daily_url()
#     monthly_url = get_monthly_url()
#     send_report_email('alherdom@outlook.com', daily_url, monthly_url)
#     time.sleep(60)
