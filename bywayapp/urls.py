from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('singlepage/<int:pk>', views.pageRoute, name='singlepage'),
    path('coursespage/', views.listCourses, name='coursespage'),
    path('ViewCategory/<int:pk>',views.ViewCategory,name='ViewCategory'),
]
