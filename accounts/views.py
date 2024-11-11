from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from .forms import UserProfileForm
from .models import UserProfile
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:client_dashboard')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



def accountSettings(request):
    # Ensure the user is in either 'default' or 'manager' group
    if not request.user.groups.filter(name__in=['default', 'manager']).exists():
        return redirect('dashboard:client_dashboard')

    # Get or create a profile for the user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = UserProfileForm(instance=profile)

    # Redirect if a profile was just created and group is 'manager'
    if created:
        if request.user.groups.filter(name='manager').exists():
            return redirect('dashboard:manager_dashboard')
        elif request.user.groups.filter(name='default').exists():
            return redirect('dashboard:client_dashboard')

    # Process the form if it's a POST request
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:account')  # Reload page after saving to show success

    # Render the account settings form
    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)
