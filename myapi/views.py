from django.shortcuts import render
from .models import BookDetails
from .models import Book
from .models import Genre
from .models import Publisher
from .models import Author
from django.shortcuts import render
from .models import *
from .serializers import *
from django.db.models.aggregates import Avg
from django.db.models.query import QuerySet
from django.utils.html import avoid_wrapping
from .forms import *
from .models import Book, BookRating
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.signals import post_save
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, response
from rest_framework.parsers import JSONParser
from typing import ContextManager
from myapi import serializers
import json
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .models import BookDetails
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

def index(request):
    num_books = Book.objects.all().count() 
    num_authors = Author.objects.count()  

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1


    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_authors': num_authors,
                 'num_visits': num_visits},
    )
    
from django.views import generic


class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book

def listauthor(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = authorserializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def authorview(request):
    form = AddAuthor()
    if request.method == "POST":
        if form.is_valid():
            form = AddAuthor(request.POST)
            Author = form.save(commit=False)
            Author.save()


    context = {'form': form}
    return render(request, 'myapi/author_detail.html', context)    


