from django.urls import path, include
from core.views import (home_view,
                        detail_view,
                        about_view,
                        team_detail,
                        menu_view,
                        events_view,
                        event_detail_view,
                        blog_view,
                        contact_view,
                        courses_view,
                        course_detail_view,
                        team_view
                        )

urlpatterns = [
    path('', home_view, name='home'),
    path('posts/<int:pk>/', detail_view, name='post_detail'),
    path('about/', about_view, name='about'),
    path('team/<int:pk>/', team_detail, name='team_detail'),
    path('menu/', menu_view, name='menu'),
    path('events/', events_view, name='events'),
    path('events/<int:pk>/', event_detail_view, name='event_detail'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact'),
    path('courses/', courses_view, name='courses'),
    path('courses/<int:pk>/', course_detail_view, name='course_detail'),
    path('team/', team_view, name='team'),

]
