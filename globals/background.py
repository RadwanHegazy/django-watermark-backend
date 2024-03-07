"""
    For create the process in background and 
    sending the email after finish
"""
from uuid import uuid4
from .watermark import Watermark as GenerateMark
from django.core.mail import send_mail
from back_end.settings import EMAIL_HOST_USER

def run (instance) : 
    user_email = instance.user.email
    extension = '.png' if instance.type == 'img' else '.mp4'
    output_path = f'media/output-data/{uuid4()}{extension}'
    
    g = GenerateMark(
        input_path=instance.original.path,
        text=instance.text,
        output_path=output_path
    )

    if instance.type == 'video' :
        g.video()
    elif instance.type == 'img':
        g.image()

    instance.output_path = output_path
    instance.save()
    
    # update the instance output after the process done

    print('worked done and the output is : ', output_path)
    print('must sending email to : ', user_email)
    send_mail(
        subject='Your post is now for free',
        html_message=f"Open your account now and show the watermark in your {instance.type}.",
        message="Process Has Been Done Successfully",
        from_email=EMAIL_HOST_USER,
        recipient_list=[user_email],
    )