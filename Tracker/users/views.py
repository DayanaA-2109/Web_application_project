from django.shortcuts import render, redirect, get_object_or_404
from .models import User

# Display all users
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


# Add User
def add_user(request):
    if request.method == "POST":
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            phone=request.POST['phone'],
            role=request.POST['role'],
            address=request.POST['address'],
            city=request.POST['city'],
            pincode=request.POST['pincode']
        )
        return redirect('user_list')

    return render(request, 'user/add_user.html')


# Update User
def update_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.phone = request.POST['phone']
        user.role = request.POST['role']
        user.address = request.POST['address']
        user.city = request.POST['city']
        user.pincode = request.POST['pincode']
        user.save()

        return redirect('user_list')

    return render(request, 'user/update_user.html', {'user': user})


# Delete User
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('user_list')