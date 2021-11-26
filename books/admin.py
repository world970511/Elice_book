from django.contrib import admin

from .forms import BookForm
from .models import BookInfo,RentInfo

# Register your models here.
@admin.register(BookInfo)
class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn','book_name', 'author', 'publisher', 'publication_date']
    list_display_links = ['book_name', 'author', 'publisher']
    search_fields = ['book_name']
    form = BookForm

@admin.register(RentInfo)
class RentHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'return_status']
    list_display_links = ['user', 'book']