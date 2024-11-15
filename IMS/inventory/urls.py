from django.urls import path
from inventory import views

urlpatterns = [
    path("dash/", views.index, name="dash"),
    path("products/", views.products, name="products"),
    path("orders/", views.orders, name="orders"),
    path("users/", views.users, name="users"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("suppliers/add/", views.add_supplier, name="add_supplier"),
    path("suppliers/edit/<int:supplier_id>/", views.edit_supplier, name="edit_supplier"),
    path("suppliers/delete/<int:supplier_id>/", views.delete_supplier, name="delete_supplier"),
]
