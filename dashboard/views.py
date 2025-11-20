from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from accounts.decorators import admin_required
from .forms import UserCreateForm, UserUpdateForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from projects.models import Project, Task
import csv


@admin_required
def dashboard_home(request):
    # Total counts
    total_users = User.objects.count()
    total_projects = Project.objects.count()
    total_active_tasks = Task.objects.filter(status__in=["pending", "in_progress"]).count()

    # Get all projects and tasks
    projects = Project.objects.all().order_by("-created_at")
    tasks = Task.objects.all().order_by("-created_at")

    return render(request, "dashboard/home.html", {
        "total_users": total_users,
        "total_projects": total_projects,
        "total_active_tasks": total_active_tasks,
        "projects": projects,
        "tasks": tasks,
    })

@admin_required
def user_list(request):
    search = request.GET.get("search", "")

    users = User.objects.filter(
        username__icontains=search
    ).order_by("id")

    paginator = Paginator(users, 10)
    page = request.GET.get("page")
    users = paginator.get_page(page)

    return render(request, "dashboard/user_list.html", {"users": users, "search": search})


@admin_required
def user_create(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("user_list")
    else:
        form = UserCreateForm()

    return render(request, "dashboard/user_form.html", {"form": form})


@admin_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserUpdateForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect("user_list")

    return render(request, "dashboard/user_form.html", {"form": form})


@admin_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("user_list")


@admin_required
def export_users_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=users.csv"

    writer = csv.writer(response)
    writer.writerow(["ID", "Username", "Email", "Role"])

    for user in User.objects.all():
        writer.writerow([user.id, user.username, user.email, user.role])

    return response
