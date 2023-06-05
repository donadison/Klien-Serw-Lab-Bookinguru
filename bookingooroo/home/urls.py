from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('check_booking/' , check_booking),
    path('home/', home , name='home'),
    path('hotel-detail/<uid>/' , hotel_detail , name="hotel_detail"),
    path('register/', register , name='register'),
    path('login1/', login1, name='login1'),
    path('login1.html', login1, name='login1')

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()