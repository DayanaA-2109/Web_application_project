
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


from django.http import HttpResponse

from django.shortcuts import redirect

def register(request):
    if request.method == "POST":
        role = request.POST.get("role")

        if role == "Admin":
            return redirect("admin_dashboard")
        elif role == "User":
            return redirect("user_dashboard")
        elif role == "Agent":
            return redirect("agent_dashboard")
        elif role == "Merchant":
            return redirect("merchant_dashboard")
        from django.shortcuts import redirect

def login_user(request):

    if request.method == "POST":

        role = request.POST.get("role")

        if role == "Admin":
            return redirect("admin_dashboard")

        elif role == "User":
            return redirect("user_dashboard")

        elif role == "Agent":
            return redirect("agent_dashboard")

        elif role == "Merchant":
            return redirect("merchant_dashboard")

    return redirect("dashboard_page")
