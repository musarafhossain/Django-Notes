from django.contrib import admin
from django.urls import path
from sayhello import views as sayhello_views
from saybye import views as saybye_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', sayhello_views.sayHello),
    path('bye/', saybye_views.sayBye),
]
