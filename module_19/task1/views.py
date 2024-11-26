from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister

# Create your views here.
def platform(request):
    title = 'Магазин ретро-игр'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'fourth_task/platform.html', context)

def shop(request):
    title = 'Магазин'
    text = 'Магазин'
    context = {
        'title': title,
        'text': text,
        #'games:': ['Doom II', 'Warcraft', 'Vikings'],
        'games': ['Doom II', 'Warcraft', 'Vikings']
    }
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    title = 'Корзина'
    text = 'Корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'fourth_task/cart.html', context)


def sign_up_by_django(request):
    users = ['Otto', 'Moritz', 'Ruslan', 'Finduss', 'Karl']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)  # обращение request.POST не забыть
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])


            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                # info.update({'error': 'Пользователь уже существует.'})
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'fifth_task/registration_page.html', info)


    else:
        info = {
            'form': UserRegister()
        }

    return render(request, 'fifth_task/registration_page.html', info)  # передача словаря без переменной не работает
    # return render(request, 'registration_page.html', {'form': form}) # не работает


def sign_up_by_html(request):
    users = ['Otto', 'Moritz', 'Ruslan', 'Finduss', 'Karl']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users:
            info['error'] = 'Пользователь уже существует.'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают.'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18.'
        else:
            info['information'] = 'Приветствуем, %s!' % username
            return render(request, 'registration_page.html', info)
            # return HttpResponse('Приветствуем, %s!' % username)

    return render(request, 'fifth_task/registration_page.html', info)