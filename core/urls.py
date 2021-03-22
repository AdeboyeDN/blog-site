from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('create/', views.blogCreateView.as_view(), name='create'),
    path('', views.blogListView.as_view(), name='home'),
    path('<str:slug>/<str:pk>/', views.blogDetailView.as_view(), name='detail'),
    path('update/<str:slug>/<str:pk>/', views.blogUpdateView.as_view(), name='update'),
    path('delete/<str:slug>/<str:pk>/', views.blogDeleteView.as_view(), name='delete'),


]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)