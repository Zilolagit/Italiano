from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class Author(models.Model):
    image = models.ImageField(upload_to='author_images/')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    featured_image = models.ImageField(upload_to='post_images/')
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.ImageField(upload_to='post_images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"{self.image}"

class Booking(models.Model):
    class StatsChoices(models.TextChoices):
        NEW = "new", "New"
        COMPLETED = "completed", "Completed"
    name = models.CharField(max_length=255)
    email = models.EmailField()
    guests = models.IntegerField()
    date = models.CharField(max_length=255)
    status = models.CharField(choices=StatsChoices, max_length=255, default=StatsChoices.NEW)
    def __str__(self):
        return f"{self.name} - {self.status}"

class Team(models.Model):
    image = models.ImageField(upload_to='team_images/')
    short_description = models.TextField()
    description = models.TextField()
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Teammates"

    def __str__(self):
        return self.name

class Event(models.Model):
    image = models.ImageField(upload_to='event_images/')
    bg_image = models.ImageField(upload_to='event_images/')
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    event_type = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class EventImage(models.Model):
    image = models.ImageField(upload_to='event_images/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"{self.image}"

class Contact(models.Model):
    class ServiceChoices(models.TextChoices):
        INQUIRY = "inquiry", "Inquiry"
        RESERVATION = "reservation", "Reservation"
        OTHER = "other", "Other"
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    service_type = models.CharField(choices=ServiceChoices, max_length=30, default=ServiceChoices.INQUIRY)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.TextField()
    cuisine = models.CharField(max_length=255)
    perfect_for = models.CharField(max_length=255)
    includes = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class CourseBooking(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    size = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.course} - {self.size}"