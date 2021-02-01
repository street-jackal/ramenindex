from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project
from projects.forms import ProjectForm 

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from projects.forms import SignUpForm
from colorthief import ColorThief

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


class CreatePostView(LoginRequiredMixin, CreateView): 

    model = Project
    #set_colors(model)
    form_class = ProjectForm
    template_name = 'post.html'
    success_url = reverse_lazy('project_index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/projects')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
