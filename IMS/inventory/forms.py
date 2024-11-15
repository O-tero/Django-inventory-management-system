from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from inventory.models import Product, Order, Supplier


class UserRegistry(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "quantity", "description"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "contact_info", "address", "email"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Supplier Name"}
            ),
            "contact_info": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contact Information",
                    "rows": 3,
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Supplier Address",
                    "rows": 3,
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Supplier Email"}
            ),
        }
