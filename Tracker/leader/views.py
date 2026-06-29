from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

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
# Add these to your existing views.py file

def add_delivery(request):
    """Add a new delivery"""
    if request.method == 'POST':
        # Your delivery creation logic here
        pass
    return render(request, 'add_delivery.html')

def update_delivery(request, id):
    """Update an existing delivery"""
    # Your delivery update logic here
    return render(request, 'update_delivery.html')

def delete_delivery(request, id):
    """Delete a delivery"""
    # Your delivery delete logic here
    return redirect('admin_dashboard')


from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect




def home(request):
    return render(request, "index.html")


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
    return render(request, "register.html")  # Added return for GET request


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


# ============================================
# DASHBOARD VIEWS (These were missing!)
# ============================================

def admin_dashboard(request):
    """Admin dashboard view"""
    context = {
        'title': 'Admin Dashboard',
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, 'admin_dashboard.html', context)


def user_dashboard(request):
    """User dashboard view"""
    context = {
        'title': 'User Dashboard',
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, 'user_dashboard.html', context)


def agent_dashboard(request):
    """Agent dashboard view"""
    context = {
        'title': 'Agent Dashboard',
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, 'agent_dashboard.html', context)


def merchant_dashboard(request):
    """Merchant dashboard view"""
    context = {
        'title': 'Merchant Dashboard',
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, 'merchant_dashboard.html', context)


def dashboard_page(request):
    """Main dashboard page"""
    context = {
        'title': 'Dashboard',
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, 'dashboard.html', context)


# ============================================
# DELIVERY CRUD VIEWS (These were also missing!)
# ============================================

def add_delivery(request):
    """Add a new delivery"""
    if request.method == 'POST':
        # Your delivery creation logic here
        # Example:
        # delivery_data = request.POST
        # delivery = Delivery.objects.create(...)
        # messages.success(request, 'Delivery added successfully!')
        return redirect('admin_dashboard')

    # For GET request - show add delivery form
    return render(request, 'add_delivery.html')


def update_delivery(request, id):
    """Update an existing delivery"""
    if request.method == 'POST':
        # Your delivery update logic here
        # Example:
        # delivery = Delivery.objects.get(id=id)
        # delivery.status = request.POST.get('status')
        # delivery.save()
        # messages.success(request, f'Delivery {id} updated successfully!')
        return redirect('admin_dashboard')

    # For GET request - show update form with delivery data
    context = {
        'delivery_id': id,
    }
    return render(request, 'update_delivery.html', context)


def delete_delivery(request, id):
    """Delete a delivery"""
    if request.method == 'POST':
        # Your delivery delete logic here
        # Example:
        # delivery = Delivery.objects.get(id=id)
        # delivery.delete()
        # messages.success(request, f'Delivery {id} deleted successfully!')
        return redirect('admin_dashboard')

    # For GET request - show confirmation page
    context = {
        'delivery_id': id,
    }
    return render(request, 'delete_delivery.html', context)