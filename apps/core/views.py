from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from apps.job.models import Job
from apps.userprofile.models import UserProfile


def frontpage(request):
    jobs = Job.objects.all()
    return render(request, "core/frontpage.html", {'jobs': jobs})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_type = request.POST.get('account_type', 'jobseeker')
            UserProfile.objects.create(
                user=user,
                is_employer=account_type == 'employer'
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, "core/signup.html", {'form': form})