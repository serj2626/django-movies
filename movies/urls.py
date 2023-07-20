from django.urls import path
from .views import MoviesView, MovieDetailView, AddReview, ActorView, FilterMoviesView

urlpatterns = [
    path('', MoviesView.as_view(), name='home'),
    path("filter/", FilterMoviesView.as_view(), name='filter'),
    path('<slug:slug>', MovieDetailView.as_view(), name='movie-detail'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", ActorView.as_view(), name="actor_detail"),

]
