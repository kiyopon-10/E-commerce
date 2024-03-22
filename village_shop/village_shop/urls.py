from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apis.urls')),
    path('account/', include('user_app.urls')),
    
    #path("api-auth/", include('rest_framework.urls')),    #This is for temporary login purpose
]

