from django.shortcuts import render, redirect
from .models import User, Video
from .forms import SearchForm, RegForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.
def home_page(request):
    # Достаем данные из БД
    videos = Video.objects.all()

    form = SearchForm

    # Отправляем данные на фронт
    context = {'videos': videos, 'form': form}

    return render(request, 'home.html', context)


def video_page(request, pk):
    # Достаем данные из БД
    video = Video.objects.get(id=pk)
    # Отправляем данные на фронт
    context = {'video': video}
    return render(request, 'video.html', context)

def user_page(request):
    user = User.objects.all()
    context = {'user': user}

    return render(request, 'user.html', context)

def comment_page(request):
    comment = Comment.objects.all()
    context = {'comment': comment}

    return render(request, 'comment.html', context)

def search(request):
    if request.method == "POST":
        get_product = request.POST.get('search_bar')

        if Video.objects.get(video_title__iregex=get_product):
            exact_product = Video.objects.get(video_title__iregex=get_product)
            return redirect(f'/video/{exact_product.id}')
        else:
            print('Не нашел')
            return redirect('/')


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(username=username, email=email, password=password2)
            user.save()
            login(request, user)
            return redirect('/')
        # Если данные не корректны
        context = {'form': RegForm}
        return render(request, self.template_name, context)

def logout_view(request):
    logout(request)
    return redirect('/')