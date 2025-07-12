from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.register_user),
    path('login/', obtain_auth_token),
    path('logout/', views.logout_user),

    path('products/', views.list_products),
    path('products/<int:pk>/', views.get_product),
    path('products/create/', views.create_product),
    path('products/<int:pk>/update/', views.update_product),
    path('products/<int:pk>/delete/', views.delete_product),

    path('reviews/create/', views.submit_review),
    path('reviews/<int:product_id>/', views.get_reviews),
]