from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    template = 'Test/index.html'
    context = {
        'form': UserCreationForm()
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username)
        if password1 == password2:
            user = User.objects.create(username = username, password= password1)
            login(request, user)
            return redirect('homes')
    return render(request, template, context)