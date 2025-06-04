import django.contrib.auth.forms as forms
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views import generic
from django.urls import reverse_lazy

def index(request):
    a = 5
    b = a**2
    c = 4
    p = [13, "Liška", 999.99]
    return render(request, "calen/index.html", {"a": a, "mocnina": b, "kriterium": c, "pole":p})

def kolo(request):
    return HttpResponse("Stránka s koly!")


def udalosti(request):
    ud = Udalost.objects.all()
    return render(request, "calen/udalosti.html", {"udalosti": ud})

@login_required
def detail(request, udalost_id):
    ud = get_object_or_404(Udalost, pk=udalost_id)
    return render(request, "calen/detail_udalosti.html", {"udalost": ud})

class RegisterView(generic.CreateView):
    template_name = "calen/register.html"
    success_url = reverse_lazy("calen:udalosti")
    form_class = forms.UserCreationForm

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("calen:udalosti"))

def log_in(request):
    form = forms.AuthenticationForm(request)
    msg = ""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy("calen:udalosti"))
    elif request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            msg = "ŠPATNÉ JMÉNO NEBO HESLO"
            return render(request, template_name="calen/login.html", context={'form': form, 'msg': msg})
        else:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy("calen:udalosti"))
    else:
        return render(request, 'calen/login.html', {'form':form, 'msg':msg})
