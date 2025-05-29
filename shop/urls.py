from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from . import views
from django.conf import settings

urlpatterns = [
    path('', views.manage_shop, name='manage-shop'),
    path('add-category/', views.add_category, name='add-category'),
    path('update-category/<str:pk>', views.update_category, name='update-category'),
    path('delete-category/<str:pk>', views.delete_category, name='delete-category'),
    path('add-product/', views.add_product, name='add-product'),
    path('update-product/<str:pk>', views.update_product, name='update-product'),
    path('delete-product<str:pk>', views.delete_product, name='delete-product'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
