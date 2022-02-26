from django.conf import settings
from django.core.mail import send_mail


def send_email_token(email,token):

    try:
        subject = 'Activate Your PriceActionAlerts Account'
        message = f"Hi, thank you for registering with PriceActionAlerts. Click on the http://{settings.ALLOWED_HOSTS[0]}:8000/account/verify/{token}/ to activate your account."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        print("Activate Your PriceActionAlerts Account: {} and {}".format(email_from,recipient_list))
        send_mail(subject, message, email_from, recipient_list)

    except Exception as e:
        print("Send Activation Email Error:",str(e))
        return False

    return True
