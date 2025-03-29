from unicodedata import category

from django.shortcuts import render, get_object_or_404, redirect

from core.models import Menu, Category, Post, PostImage, Booking, Team, Event, EventImage, Contact, Course, \
    CourseBooking


def home_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        guests = request.POST.get("guests")

        data = {
            "name" : name,
            "email" : email,
            "date" : date,
            "guests" : guests
        }
        Booking.objects.create(**data)
        return redirect(request.get_full_path())

    food_menu = Category.objects.filter(name='Food').first()
    foods = Menu.objects.filter(category=food_menu)
    wine_menu = Category.objects.filter(name='Wine').first()
    wines = Menu.objects.filter(category=wine_menu)
    posts = Post.objects.all()[:2]

    context = {
        "wf": '{"path":"symbol","type":"PlainText"}',
        "foods" : foods,
        "wines" : wines,
        "posts" : posts,

    }
    return render(request, 'core/index.html', context)

def detail_view(request, pk):
    post = get_object_or_404(Post.objects.all(), pk=pk)
    images = PostImage.objects.filter(post=post)
    context = {
        "post" : post,
        "images" : images,
        "wf": '{"path":"symbol","type":"PlainText"}',
    }
    return render(request, 'core/blog/post_detail.html', context)

def about_view(request):
    team = Team.objects.filter(featured = True)
    context = {
        "teammates" : team[:3]
    }
    return render(request, 'core/about-us.html', context)

def team_detail(request, pk):
    team = get_object_or_404(Team.objects.all(), pk=pk)
    context = {
        "team" : team,
    }
    return render(request, 'core/teams/team_detail.html', context)

def menu_view(request):
    foods = Menu.objects.filter(category__name='Food')
    wines = Menu.objects.filter(category__name='Wine')
    sweets = Menu.objects.filter(category__name='Sweets')
    context = {
        "foods" : foods,
        "wines" : wines,
        "sweets" : sweets,
    }
    return render(request, 'core/menu.html', context)

def events_view(request):
    events = Event.objects.all()
    context = {
        "events" : events,
    }
    return render(request, 'core/events.html', context)

def event_detail_view(request, pk):
    event = get_object_or_404(Event.objects.all(), pk=pk)
    images = EventImage.objects.filter(event_id = pk)
    context = {
        "event" : event,
        "images" : images
    }
    return render(request, 'core/events/event_detail.html', context)

def blog_view(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, 'core/blog.html', context)

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        service_type = request.POST.get("service_type")
        message = request.POST.get("message")
        number = request.POST.get("number")
        data = {
            "name" : name,
            "email" : email,
            "service_type" : service_type,
            "phone_number" : number,
            "message" : message
        }
        Contact.objects.create(**data)
    return render(request, 'core/contact-us.html')

def courses_view(request):
    courses = Course.objects.all()
    context = {
        "courses" : courses
    }
    return render(request, 'core/category/courses.html', context)

def course_detail_view(request, pk):
    if request.method == "POST":
        guests = request.POST.get("guests")
        number = request.POST.get("number")
        CourseBooking.objects.create(course_id = pk, quantity=number, size=guests)
    course = get_object_or_404(Course.objects.all(), pk=pk)

    context = {
        "course" : course,
    }
    return render(request, 'core/product/course_detail.html', context)

def team_view(request):
    teams = Team.objects.all()
    context = {
        "teammates" : teams
    }
    return render(request, 'core/teams.html', context)