# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:40:32 2019

@author: nobody
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)