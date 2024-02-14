"""
URL configuration for smartlibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from app.admin import admin_site
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from app.views import BookRatingAPIView, BookViewSet, RatingCreateAPIView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/')),
    path('admin/', admin_site.urls),  # Use the custom admin site URLs
    path('api/', include(router.urls)),
    path('api/rate/', RatingCreateAPIView.as_view(), name='rate-book'),
    path('api/book/<int:book_id>/rating/<str:user_id>/', BookRatingAPIView.as_view(), name='book-rating')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)