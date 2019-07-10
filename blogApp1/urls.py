# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:39:24 2019

@author: nobody
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]