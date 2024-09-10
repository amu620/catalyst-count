from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # allauth URLs for user authentication
    
]
