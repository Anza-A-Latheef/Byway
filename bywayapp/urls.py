from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('clickbutton/',views.clickbutton,name='clickbutton'),

]
