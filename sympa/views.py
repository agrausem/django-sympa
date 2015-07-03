# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def users(request):
    active_users = User.objects.filter(is_active=True).exclude(email='')
    return render(request, 'users.sympa', {'users': active_users},
                  content_type='text/plain')
