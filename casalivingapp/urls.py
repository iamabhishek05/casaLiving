from django.urls import path
from .import views


from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [

    path("", views.index, name="homepage"),
    path("houses", views.houses, name="houses"),
    path("aboutus", views.about, name="about"),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('schedule-visit/', views.schedule_visit, name='schedule_visit'),
    path('home_schedule-visit/', views.home_schedule_visit, name='home_schedule_visit'),
    # path("contact", views.contact, name="contact"),

  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)