from django.urls import path
from .views import AboutView, SnackDeleteView, SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView

urlpatterns = [
        path('', SnackListView.as_view(), name='snack_list'),
        path("<int:pk>/", SnackDetailView.as_view(), name='snack_detail'),
        path('about/', AboutView.as_view(), name='about'),
        path('create/', SnackCreateView.as_view(), name='snack_create'),
        path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),
        path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
]