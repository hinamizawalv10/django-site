from django.shortcuts import render
import datetime
# from django.contrib.auth.decorators import login_required  ← この行は不要

# @login_required ← この行は不要
def index(request):
    now = datetime.datetime.now()
    context = {
        'current_time': now,
    }
    return render(request, 'main/index.html', context)