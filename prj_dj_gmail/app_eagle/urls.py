from django.urls    import path
from app_eagle      import views

app_name = 'app_eagle'
urlpatterns = [
    path( ''             , views.home        , name= 'home1'         ),
    path( 'home/'        , views.home        , name= 'home'         ),
    path( 'write_mail/'  , views.write_mail  , name= 'write_mail'   ),
    path( 'mail_sent_ok/', views.mail_sent_ok, name= 'mail_sent_ok' ),
]