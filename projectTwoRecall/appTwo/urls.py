from django.conf.urls import url
from appTwo import views

app_name = 'appTwo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^users/$', views.users, name='userPage'),
    # url(r'^users/form/', views.userForms, name='userFormPage'),
    url(r'^user/registeration/*$', views.registeration, name='registerationPage'),
    url(r'^user/login/*$', views.userLogin, name='loginPage')
    # url(r'^test/', views.test)
]
