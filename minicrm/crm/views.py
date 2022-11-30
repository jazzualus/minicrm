from django.shortcuts import render
from django.http import HttpResponse
from .models import Region, Status, Customer, Activity, ActivityType
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def activities(request):
    activities = Activity.objects.all()
    context = {
        'activities': activities
    }
    print(activities)
    return render(request, 'activities.html', context=context)


def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    print(activities)
    return render(request, 'customers.html', context=context)


class ActivityDetailView(generic.DetailView):
    model = Activity
    template_name = 'activity_detail.html'


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')