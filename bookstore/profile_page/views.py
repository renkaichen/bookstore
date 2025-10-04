from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Order

@login_required
def index(request):
    template_data = {}
    template_data['title'] = 'Profile'
    template_data['username'] = request.user.username
    template_data['orders'] = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile/index.html', {'template_data': template_data})
