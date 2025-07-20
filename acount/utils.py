import random, string
from django.core.mail import send_mail
from conf.settings import DEFAULT_FROM_EMAIL
def generic_code():
    letter = string.ascii_letters + string.digits
    return ''.join([letter[random.randint(0,len(letter) -1)] for _ in range(6)])


def send_to_mail(email,code):
    subject = 'Tastiqlash kodi'
    message = f"sizning kodingiz {code}"
    send_mail(subject=subject, message=message, from_email=DEFAULT_FROM_EMAIL, recipient_list=[email,])
