from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.user.role != "ADMIN":
            messages.error(request, "Access Denied!")
            return redirect("profile")
        return view_func(request, *args, **kwargs)
    return wrapper
def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.user.role not in ["MANAGER"]:
            messages.error(request, "Access Denied! Managers only.")
            return redirect("profile")
        return view_func(request, *args, **kwargs)
    return wrapper
