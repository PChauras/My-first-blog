from django import forms

from .models import Post
from .models import Input_number

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

class InputForm(forms.ModelForm):

	class Meta:
		model = Input_number
		fields = ('input_x',)