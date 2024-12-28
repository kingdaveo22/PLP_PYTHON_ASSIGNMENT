import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProductForm
from .models import Product

# Replace with your actual Stripe keys
stripe.api_key = 'your_stripe_secret_key' 

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('thank_you')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def thank_you(request):
    return render(request, 'store/thank_you.html')

def home(request):
    return render(request, 'store/home.html')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.save()
            return redirect('home') 
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

@login_required
def inventory(request):
    products = Product.objects.filter(vendor=request.user)
    return render(request, 'store/inventory.html', {'products': products})

@login_required
def create_checkout_session(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/', 
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({'id': session.id})