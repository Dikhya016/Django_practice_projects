from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/',views.index,name='index'),
    path('details/<int:id>/',views.details,name='details'),
    path('create/',views.createitem,name='createitem'),
    path('update/<int:id>/',views.updateitem,name='updateitem'),
    path('delete/<int:id>/',views.deleteitem,name='deleteitem'),
]