from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
# Create your views here.
def home_page(request):
    return render(request,'index.html')


def register_user(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, f'Account for username {username} successfully created.')
        return redirect('home_page')
  else:
      form = SignUpForm() 
  return render(request, 'registration/registration_form.html', {'form': form})   



def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse("home_page"))
            else:
                return HttpResponseRedirect(reverse("user_login")) 

        else:
            return HttpResponseRedirect(reverse("user_login")) 
    else:
        return render(request, "registration/login_form.html", context={})  


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))        
