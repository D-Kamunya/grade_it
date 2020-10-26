from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,ProjectForm,RatingsForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Project,Rating
# Create your views here.
def home_page(request):
    projects=Project.get_all_projects()
    context={
        'projects':projects
    }
    return render(request,'index.html',context)


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



@login_required(login_url='/accounts/login/')
def submit_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, f'Project successfully uploaded')
            form = ProjectForm() 
    else:
        form = ProjectForm()  


    context={
        "form":form
    }

    return render(request,'new_project.html',context)



def get_project_ratings_av(prj_id):
    ratings=Rating.get_project_ratings(prj_id)
    if ratings:
        design_ratings = [int(d.design) for d in ratings]
        design_avg = round(sum(design_ratings) / len(design_ratings),2)

        usability_ratings = [int(us.usability) for us in ratings]
        usability_avg = round(sum(usability_ratings) / len(usability_ratings),2)

        content_ratings = [int(content.content) for content in ratings]
        content_avg = round(sum(content_ratings) / len(content_ratings),2)

        score_avg = round((design_avg+usability_avg+content_avg)/3,2)
        
        av_ratings={
            'design':design_avg,
            'usability':usability_avg,
            'content':content_avg,
            'score':score_avg,
        }
        return av_ratings
    else:
        av_ratings={
        'design':0.00,
        'usability':0.00,
        'content':0.00,
        'score':0.00,
        }
        return av_ratings

   


@login_required(login_url='/accounts/login/')
def view_project(request,prj_id):
    project = Project.get_project_by_id(prj_id)
    ratings=get_project_ratings_av(prj_id)
    raters=Rating.get_project_ratings(prj_id)
    already_rated=False
    for user in raters:
        if request.user==user.user:
            already_rated=True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            design=int(request.POST.get("design"))
            usability=int(request.POST.get("usability"))
            content=int(request.POST.get("content"))
            score=round((design+usability+content)/3,2)
            rate.score=score
            rate.save()
            messages.success(request, f'You rated this project')
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    context = {
        'project': project,
        'form': form,
        'ratings':ratings,
        'raters':raters,
        'already_rated':already_rated
    }

    return render(request,'project.html',context)    