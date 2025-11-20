from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def my_tasks(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        new_status = request.POST.get("status")

        task = Task.objects.get(id=task_id, assigned_to=request.user)
        task.status = new_status
        task.save()

        return redirect("my_tasks")

    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, "projects/my_tasks.html", {"tasks": tasks})
