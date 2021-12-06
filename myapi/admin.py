from django.contrib import admin
from .models import BookDetails
from .models import Book
from .models import Genre
from .models import Publisher
from .models import Author
admin.site.register(BookDetails)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Author)
