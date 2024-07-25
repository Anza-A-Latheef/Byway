from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('singlepage/', views.pageRoute, name='singlepage'),
    path('coursespage/', views.listCourses, name='coursespage')
]
