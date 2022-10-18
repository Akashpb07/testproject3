from django.urls import path
from stories import views

urlpatterns = [
    path('story/<pk>/', views.StoryDetailView.as_view(), name='story-detail'),

]

