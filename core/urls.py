from django.contrib import admin
from django.urls import path, include
from home.views import home, checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('checkout', checkout, name="checkout"),
]
