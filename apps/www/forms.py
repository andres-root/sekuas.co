# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core import validators

class newPostForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput())
	content = forms.CharField(widget=forms.Textarea())

	def clean(self):
		return self.cleaned_data

class newSong(forms.Form):
	title = forms.CharField(widget=forms.TextInput())
	description = forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data


class SUCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password','is_superuser')
