import json

from django.shortcuts       import render, redirect
from django.conf            import settings
from django.core.mail       import send_mail, EmailMessage

from . import forms

# Create your views here.

def home( request ):
    return render( request, 'gui/home.html' )    

def write_mail( request ):
    letter  = {
                'to'      : 'my-friend@hotmail.com',
                'subject' : 'hello'
                'msg'     : 'have a happy day 🦊',
            }

    form    = forms.LetterForm( initial= letter )
    dic     = {}

    if request.method=='POST':
        form = forms.LetterForm( request.POST )
        if form.is_valid():
            to  = form.cleaned_data[ 'to'  ],
            msg = form.cleaned_data[ 'message'    ],

            mail_sent = send_mail(subject,
                message,
                settings.EMAIL_HOST_USER,
                [ to ] )            
            
            return redirect( 'app_eagle:mail_sent_ok' )
            #return render(request, '/gui/mail_sent_ok.html' )

    dic[ 'form' ] = form
    return render( request, 'gui/write_mail.html', dic )

def mail_sent_ok( request ):
    return render(request, 'gui/mail_sent_ok.html')


