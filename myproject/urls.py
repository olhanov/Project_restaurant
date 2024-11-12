from django.contrib import admin
from django.urls import path
from restaurant import views
from django.conf import settings
from django.conf.urls.static import static







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),  # Маршрут для головної сторінки
    path('menu/', views.menu_view, name='menu'),
    path('test/', views.test, name='test'),  # Маршрут для тестової сторінки
    path('reservation/', views.reservation_view, name='reservation'),
    path('galeria/', views.gallery_view, name='galeria'),
    path('sobre-nos/', views.sobre_nos_view, name='sobre-nos'),
    path('contactos/', views.contactos_view, name='contactos'),
    path('reservas/', views.reservas_view, name='reservas'),
    path('search/', views.search_view, name='search'),

    path('my_account/', views.login_view, name='my_account'),
    path('personal_account/', views.personal_account, name='personal_account'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/get_user_comment_data/<int:comment_id>/', views.get_user_comment_data, name='get_user_comment_data'),

    
   

   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
