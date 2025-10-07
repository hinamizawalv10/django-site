from django.shortcuts import render
import datetime
from django.contrib.auth.decorators import login_required # 1. これを追加

@login_required # 2. この行を追加
def index(request):
    now = datetime.datetime.now()
    context = {
        'current_time': now,
    }
    return render(request, 'main/index.html', context)