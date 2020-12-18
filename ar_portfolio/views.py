from django.shortcuts import render, redirect
from .form import UserForm
from django.contrib import messages

def portfolio_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
       
        if form.is_valid:
            form.save()
            messages.success(request, f'Your form has been submitted.')
            return redirect('portfolio_home')
    else:
        form = UserForm()
    return render(request, "ar_portfolio/portfolio.html", {"form": form})
