from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Input_number
from .forms import PostForm
from .forms import InputForm



# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = '1'#request.user
			post.published_date = timezone.now()
			post.save()
			#return redirect('blog.view.post_new')
			return render(request, 'blog/post_edit.html', {'form': form})
	else:
		form = PostForm()
		return render(request, 'blog/post_edit.html', {'form': form})

def post_calc(request):
	if  request.method == "POST":
		form = InputForm(request.POST)
		#if form.is_valid():
		input_ = form.save(commit=False)
		input_.calc_square = input_.input_x ** (2)
		input_.save()
		
		input_s = Input_number.objects.filter(input_x=input_.input_x)
			#return redirect('blog.view.post_new')
		return render(request, 'blog/post_calc.html', {'form': form, 'input_s': input_s})
	else:
		form = InputForm()
		return render(request, 'blog/post_input.html', {'form': form})
