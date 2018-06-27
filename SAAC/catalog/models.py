from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid

# Create your models here.
class Batch(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    year = models.CharField(max_length=200, help_text="Enter your year")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.year


class Student(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    id = models.CharField(primary_key=True, max_length = 10)
    name = models.CharField(max_length=200)
    # branch = models.ForeignKey('Programme', on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length = 70)
    year = models.ManyToManyField(Batch, help_text='Select year')
    attendance = 0
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    def present(self):
        self.attendance += 1

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('student-detail', args=[str(self.id)])
    class Meta:
        ordering = ["id"]
