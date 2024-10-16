from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('katalog', views.katalog, name='katalog'),
    path('', views.homepage, name='home'),
    path('adminpage/', views.dashboard, name='dashboard'),
    path('adminpage/update/<int:produks_id>', views.produks_update, name='produks_edit'),
    path('adminpage/delete/<int:produks_id>', views.produks_delete, name='produks_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)