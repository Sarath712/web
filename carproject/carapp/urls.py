from django.conf.urls.static import static
from django.urls import path

from carproject import settings
from . import views

app_name = 'carapp'

urlpatterns = [
    path('',views.index, name='index'),
    path('car/<int:car_id>/',views.detail,name='detail'),
    path('add/',views.add_car, name='add_car'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)