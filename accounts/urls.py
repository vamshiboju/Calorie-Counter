from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('BMICALC',views.BMICALC,name='BMICALC'),
    path('calorie',views.calorie,name='calorie'),
    path('diet',views.diet,name='diet'),
    path('workout',views.workout,name='workout')
]
