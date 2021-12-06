from django.db import models
from django.urls import reverse


class Book(models.Model):
    ISBN = models.CharField(max_length=60)
    Title = models.CharField(max_length=60)
    Description = models.CharField(max_length=60)
    PublishDate = models.DateField()

    def __str__(self):
        return self.Title


class Genre(models.Model):
    GenreID = models.CharField(max_length=60)
    Type = models.CharField(max_length=60)

    def __str__(self):
        return self.Type


class Publisher(models.Model):
    PublisherID = models.CharField(max_length=60)
    Name = models.CharField(max_length=60)

    def __str__(self):
        return self.Name


class Author(models.Model):
    AuthorID = models.CharField(max_length=60)
    FName = models.CharField(max_length=60)
    LName = models.CharField(max_length=60)
    Biography = models.CharField(max_length=60)

    class Meta:
        ordering = ['LName', 'FName']

    def get_absolute_url(self):

        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.LName, self.FName)


class BookDetails(models.Model):
    ID = models.CharField(max_length=60)
    Price = models.CharField(max_length=60)
    CopiesSold = models.CharField(max_length=60)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    GenreID = models.ForeignKey(Genre, on_delete=models.CASCADE)
    PublisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    AuthorID = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['ISBN', 'AuthorID']

    def display_genre(self):
        return ', '.join([genre.type for genre in (self.genre, all()[:3])])

    display_genre.short_description = 'Genre'
