from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def index(request): # Home Page?
    return HttpResponse("Welcome to the Library!")

# So, for books, we require the following pages:
#   Add a book (admin/lib)
def add_book(request):
    return HttpResponse("Adding new book to the Library!")
#   Delete a book (admin/lib)
def delete_book(request, book_id):
    return HttpResponse("Deleting book {0} from the Library!".format(book_id))
#   View book details
def show_book_details(request, book_id):
    return HttpResponse("Listing details for book {0}".format(book_id))
#   Edit book details (admin/lib)
def edit_book(request, book_id):
    return HttpResponse("Editing details for book {0}".format(book_id))
#   Search for a book
def search_for_book(request): # Don't know how we will handle this yet...
    return HttpResponse("Lost, lost, lost")
#   List Books (search without criteria?)
def list_books(request):
    return HttpResponse("Here is a list of our books:")



# For transactions we need to:
# 1. Checkout books (auth)
# 2. Reserve Books (auth)
#   The librarian should also be able to serve as a proxy for others

# 3. View transactions (Librarian should be able to view all, and dump to file
