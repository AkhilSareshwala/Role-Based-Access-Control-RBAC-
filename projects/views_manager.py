from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import manager_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Project List
@manager_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})

# Create Project
@manager_required
def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.created_by = request.user
        project.save()
        return redirect("project_list")
    return render(request, "projects/project_form.html", {"form": form})

# Edit Project
@manager_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect("project_list")
    return render(request, "projects/project_form.html", {"form": form})

# Delete Project
@manager_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect("project_list")


# TASKS
@manager_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "projects/task_list.html", {"tasks": tasks})

@manager_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("task_list")
    return render(request, "projects/task_form.html", {"form": form})

@manager_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("task_list")
    return render(request, "projects/task_form.html", {"form": form})

@manager_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_list")
