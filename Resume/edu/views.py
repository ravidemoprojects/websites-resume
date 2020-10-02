from django.shortcuts import render

# Create your views here.
def skills(request):
    context= {'skill': 'active'}
    return render(request, 'edu/skills.html', context)