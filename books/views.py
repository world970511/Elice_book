from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import BookInfo

# Create your views here.
class BookListView(ListView):
    model = BookInfo
    paginate_by = 10
    context_object_name = 'books'

@login_required
def rent(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(BookInfo, pk=pk)
        book.rent_book(request.user)
        messages.info(request, '대여 완료.')
        return redirect('account:mybook')
    else:
        return redirect('books:list')

@login_required
@require_POST
def return_book(request, pk):
    book = get_object_or_404(BookInfo, pk=pk)
    if book.rent_info.user == request.user:
        book.return_book()
    else:
        messages.error(request, '문제가 발생했습니다.')
    return redirect('account:mybook')