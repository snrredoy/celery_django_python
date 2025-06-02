from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def add1(x, y):
    sleep(10)
    return x + y

@shared_task
def sub(x, y):
    sleep(10)
    return x - y

@shared_task
def send_email():
    send_mail(
        'Your account is hacked.',
        'Your account is hacked by SNR. Send your bank account number to this email. SNR is a good person.',
        'towhidulislam.mail@gmail.com',
        ['choyon.ugv@gmail.com'],
        fail_silently=False,
    )
