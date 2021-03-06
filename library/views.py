from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from .models import Book
from .forms import BookForm
# Create your views here.


def index(request): # Home Page?
    return HttpResponse("Welcome to the Library!")


def add_book(request):  # (Admin/lib only)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/library/books') # Try to decouple this
    else:
        form = BookForm()
    return render(request, 'library/newbook.html', {'form': form})
        
def delete_book(request, book_id):  # (Admin/lib only)
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/library/books') # Decouple this as well

def show_book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/bookDetail.html', {'book': book})    

def edit_book(request, book_id):  # Admin/lib only)
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        form = BookForm(request.POST, instance=book)
        form.save()
        return HttpResponseRedirect('/library/books') # Decouple this as well
    else:
        book = get_object_or_404(Book, pk=book_id)
        form = BookForm(instance=book)
        return render(request, 'library/editbook.html', {'form': form, 'book_id': book_id})

def search_for_book(request): # Don't know how we will handle this yet...
    return HttpResponse("Lost, lost, lost")

def list_books(request):
    # We may want to paginate this...
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render(request, 'library/listAllBooks.html', context)




# For transactions we need to:
# 1. Checkout books (auth) (librarian as a proxy only)
# 2. Reserve Books (auth)
#   The librarian should also be able to serve as a proxy for others

# 3. View transactions (Librarian should be able to view all, and dump to file)
