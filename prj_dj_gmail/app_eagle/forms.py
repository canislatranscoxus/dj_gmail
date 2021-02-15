from django         import forms
from django.core    import validators


class LetterForm( forms.Form ):

    to      = forms.CharField( max_length = 100 )
    subject = forms.CharField( max_length = 100 )
    msg     = forms.CharField(  )

    def clean(self):
        user_cleaned_data = super().clean()