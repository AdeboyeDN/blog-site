from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('create/', views.blogCreateView.as_view(), name='create'),
    path('home/', views.blogListView.as_view(), name='home'),
    path('detail/<str:slug>/', views.blogDetailView.as_view(), name='detail'),


]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)