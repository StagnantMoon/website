from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import HoursForm

import pandas as pd


# Create your views here.


# Protect View has to be first or else errors

class ProtectedView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "redirect_to"

    # item = Hours.objects.all().values()
    # df = pd.DataFrame(item)
    # mydict = {
    #     "df": df.to_html()
    # }

    def get(self, req, *args, **kwargs):
        user = req.user

        if isinstance(user, AnonymousUser):
            return HttpResponse("You cannot access this page")
        else:
            return HttpResponse("You have access to this page.")


# Login Class View Created  Login Page but couldn't figure out the issue with protected.


class LogInView(View):
    form_class = LoginForm

    def post(self, req, *args, **kwargs):
        form = self.form_class(data=req.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(req, username=username, password=password)
            # Redirect
            if user is not None:
                login(req, user)

                redirect_to = req.GET.get("redirect_to")

                if redirect_to is None:
                    return HttpResponse("You have successfully logged in")
                else:
                    return HttpResponseRedirect("You cannot login with this account")

        else:
            return HttpResponse("Form is not valid")

    def get(self, req, *args, **kwargs):
        form = self.form_class()
        return render(
            req,
            "nwc/login.html",
            {
                "form": form,
            },
        )

        return HttpResponse("Login view")


# Logout Class


class LogoutView(View):
    def get(self, req, *args, **kwargs):
        user = req.user
        if isinstance(user, AnonymousUser):
            return HttpResponse("You have not logged in")
        else:
            logout(req)
            return HttpResponse("You have logged out")
        return HttpResponse("Logout view")


class HoursCreate(CreateView):
    model = Hours

    # Specify which fields to be displayed
    fields = ['name',
              # 'date_charity',
              'hours_work',
              'type_work',
              'service_work',
              'describe']


# To View the Database in Lists

class HoursList(ListView):
    model = Hours


# Submit and move to view of form page

def home_view(request):
    context = {}
    form = HoursForm(request.POST or None, request.FILES or None)

    # is form valid
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "nwc/hours_form.html", context)

# Class-Based Hours View Class
# class MyView(View):
#     def get(self, request):
#
#         return HttpResponse('result')


# def home(request):
# return render(request, "nwc/index.html")
# return HttpResponse("hola i am working")
# return render(request=request, template_name="nwc/home.html")


# def register(request):
# return render(request, "nwc/register.html")


# def signin(request):
# return render(request, "nwc/signin.html")


# def signout(request):
# pass

# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             messages.sucess(request, "Registration Success!")
#             return redirect("nwc:index")
#         messages.error(request, "Registration unsuccessful.")
#     form = NewUserForm()
#     return render(request=request, template_name="nwc/register.html", context={"register_form":form})
