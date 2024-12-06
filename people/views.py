from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import *
import matplotlib.pyplot as plt
from .models import *
import io
import urllib
import base64

def bar_graph_view(request):
    activities = UserActivity.objects.all()
    usernames = [activity.user.username for activity in activities]
    total_activities = [activity.total_activity() for  activity in activities]


    plt.figure(figsize=(10,6))
    plt.bar(usernames, total_activities, color= 'skyblue')
    plt.title("Total User Activity", fontsize = 16)
    plt.xlabel('User', fontsize = 12)
    plt.ylabel('total Activity', fontsize=12)
    plt. xticks(rotation = 45)
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    chart = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'users/bar_graph.html', {'chart': chart})


def pie_chart_view(request):

    activities = UserActivity.objects .all()
    usernames= [activity.user.username for activity in activities]
    total_activities = [activity.total_activity() for activity in activities]

     # Generate the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(total_activities, labels=usernames, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('User Activity Distribution', fontsize=16)

    # Convert the plot to an image in-memory
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    chart = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'users/pie_chart.html', {'chart': chart})




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            login(request, user)  # Log the user in
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('profile')  # Redirect to a desired page after login
    else:  # Handle GET requests
        form = UserRegistrationForm()  # Display an empty form
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            return redirect('profile')
    else: 
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successful')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/update_profile.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})
