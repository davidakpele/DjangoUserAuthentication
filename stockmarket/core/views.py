from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Users, user_collection
import json

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def add_record(request):
    firstname = ["Kelvin", "David", "Christian", "Ronaldo", "Ola", "Jim", "Precious", "Cynthia", "Mary", "James"]
    lastname = ["Obina", "Mark", "Samson", "Alex", "Abimbola", "Adams", "Katheria", "Neison", "Okonufua", "Ose"]
    age = ["21", "32", "44", "39", "51", "62", "18", "79", "45", "58"]
    email = ["kelvin@aol.com", "david@aol.com", "christian@aol.com", "ronaldo@aol.com", "ola@aol.com", "jim@aol.com", "precious@aol.com", "cynthia@aol.com", "bella@aol.com", "james@aol.com"]
    password = ["123", "123", "123", "123", "123", "123", "123", "123", "123", "123"]

    docs = []
    for f, l, a, e, p in zip(firstname, lastname, age, email, password):
        doc = {"firstname": f, "lastname": l, "age": a, "email": e, "password": p}
        docs.append(doc)

    user_collection.insert_many(docs)

    return HttpResponse("Data inserted successfully.")


@login_required(login_url='login')
def get_all_users(request):
    users = Users.find()
    return HttpResponse(users)

def login_view(request):
    # Your view logic can go here
    if 'lastname' in request.session and 'firstname' in request.session:
        # Both session variables are set, so redirect to the dashboard
        return redirect('../dashboard/index')
    else:
        # Render the view template or perform other actions as needed
        return render(request, 'auth/login.html')


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Check if the email and password are provided in the JSON data
            if email is None or password is None:
                return JsonResponse({'error': 'Email and password are required'}, status=400)

            # Authenticate the user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login Successful..!', 'status': 200})
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data', 'status': 400})

    return JsonResponse({'error': 'Invalid request method', 'status': 400})

@login_required(login_url='login')    
def default(request):
    return render(request, 'dashboard/index.html')
 
@login_required(login_url='login')
def updateUser_stockMarkert():
    return HttpResponse("<h1>Here will be HttpResponse on Json format </h1>")


def logout_view(request):
    logout(request)  # Log the user out and destroy their session
    return redirect('login')  # Redirect to the login page or any other page

    