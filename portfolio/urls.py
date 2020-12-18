from django.contrib import admin
from django.urls import path, include
from ar_portfolio import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ar_portfolio.urls"))
]
