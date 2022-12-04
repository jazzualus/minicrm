from django.shortcuts import render
from django.http import HttpResponse
from .models import Region, Status, Customer, Activity, ActivityType
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ActivityForm

def index(request):
    return render(request, 'index.html')


#def activities(request):
#    activities = Activity.objects.all()
#    context = {
#        'activities': activities
#    }
#    print(activities)
#    return render(request, 'activities.html', context=context)

class ActivityListView(LoginRequiredMixin, generic.ListView):
    model = Activity
    template_name = 'activities.html'
    paginate_by = 12

    def get_queryset(self):
        return Activity.objects.filter(salesman=self.request.user)


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    template_name = 'customers.html'
    paginate_by = 12

    def get_queryset(self):
        return Customer.objects.filter(salesman=self.request.user)


#def customers(request):
#    customers = Customer.objects.all()
#    context = {
#        'customers': customers
#    }
#    #print(activities)
#    return render(request, 'customers.html', context=context)


class ActivityDetailView(generic.DetailView):
    model = Activity
    template_name = 'activity_detail.html'


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
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
                    User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


#@login_required
#def profile(request):
#    return render(request, 'profile.html')

@login_required
@csrf_protect
def new_activity(request):
    form = ActivityForm()
    if request.method == 'POST':
        """
        activity_type = request.POST['activity_type']
        activity_description = request.POST['activity_description']
        sold_units = request.POST['sold_units']
        price_per_unit = request.POST['price_per_unit']
        date = request.POST['date']
        date_next_activity = request.POST['date_next_activity']
        customer = request.POST['customer']
        #salesman = self.request.user
        """
        form = ActivityForm(request.POST)
        if form.is_valid():
            #activity_type=activity_type,
        #, customer=customer

            #new_activity = Activity(activity_description=activity_description, sold_units=sold_units, price_per_unit=price_per_unit,
            #                         date=date, date_next_activity=date_next_activity, activity_type=activity_type)
            #new_activity.save()
            form.save()
            return render(request, 'activities.html')
    context = {'form': form}
    return render(request, 'new_activity.html', context)

"""
    if request.method == "POST":
        form = ActivityForm(request.POST)
        activity_type = request.POST['activity_type']
        activity_description = request.POST['activity_description']
        sold_units = request.POST['sold_units']
        price_per_unit = request.POST['price_per_unit']
        date = request.POST['date']
        date_next_activity = request.POST['date_next_activity']
        customer = request.POST['customer']

        Activity.objects.create_activity(activity_type=activity_type, activity_description=activity_description, sold_units=sold_units,
                                         price_per_unit=price_per_unit, date=date, date_next_activity=date_next_activity, customer=customer)
        return render(request, 'activities.html')
"""