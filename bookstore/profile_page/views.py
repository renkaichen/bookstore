from django.shortcuts import render
def index(request):
    template_data = {}
    template_data['title'] = 'Profile'
    return render(request, 'profile/index.html', {'template_data': template_data})
