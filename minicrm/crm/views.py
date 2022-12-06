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
from .forms import ActivityForm, CustomerForm, UserUpdateForm
from django.views.generic.edit import CreateView


def index(request):
    return render(request, 'index.html')


class ActivityListView(LoginRequiredMixin, generic.ListView):
    model = Activity
    template_name = 'activities.html'
    paginate_by = 12

    def get_queryset(self):
        print(self.request.user)
        return Activity.objects.filter(salesman=self.request.user)


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    template_name = 'customers.html'
    paginate_by = 12

    def get_queryset(self):
        return Customer.objects.filter(salesman=self.request.user)


class ActivityDetailView(generic.DetailView):
    model = Activity
    template_name = 'activity_detail.html'


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


class NewActivity(CreateView):

    model = Activity
    form_class = ActivityForm
    template_name = 'new_activity.html'
    success_url = ('activities')

    def get_from_kwargs(self):
        kwargs = super(NewActivity, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


"""
@login_required
@csrf_protect
def new_activity(request):
    form = ActivityForm()
    form.fields["salesman"].initial = request.user
    form.fields["customer"].initial = Customer.objects.filter(salesman=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities')
    print(Customer.objects.filter(salesman=request.user))
    context = {'form': form}
    return render(request, 'new_activity.html', context)
"""

@login_required
@csrf_protect
def new_customer(request):
    form = CustomerForm()
    form.fields["salesman"].initial = request.user
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    context = {'form': form}
    return render(request, 'new_customer.html', context)


@login_required
@csrf_protect
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'profile.html', context)


