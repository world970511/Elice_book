from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "books"#redirect 사용시 주의

urlpatterns = [
    path('list/', views.BookListView.as_view(),name='list'),
    url(r'^list/rent/(?P<pk>\d+)/$', views.rent, name='rent'),
    url(r'^return/(?P<pk>\d+)/$', views.return_book, name='return_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
