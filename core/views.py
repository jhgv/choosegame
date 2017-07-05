import os, json, operator
from django.shortcuts import render , redirect
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from collections import OrderedDict

from .forms import UserPreferenceForm
from .models import UserPreference, UserHiddenPreference
from .utils import get_price_interval, GENRES_LIST, get_clean_price

class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Erro")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')

    def post(self, request):
        logout(request)
        return redirect('/login/')


class LikeView(View):

    def get(self, request):
        price = float(get_clean_price(request.GET.get('price', '')))
        price_interval = get_price_interval(price)
        genre = request.GET.get('genre', '')
        platform = request.GET.get('platform', '')

        if UserHiddenPreference.objects.filter(user=request.user).count() > 0:
            up = UserHiddenPreference.objects.get(user=request.user)
            up.price = up.price + "," + price_interval
            up.genre = up.genre + "," + genre
            up.platform = up.platform  + "," + platform
            up.save()
        else:
            up = UserHiddenPreference(user=request.user, genre=genre, price=price_interval, platform=platform)
            up.save()
        return redirect('/')

class HomeView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_recommended(self, games):
        preferences = self.request.user.preferences
        recommended_games = {}
        counter = 1
        for game in games:
            score = 0

            if preferences.platform and game['plataforma'] == preferences.platform:
                score = score + 1

            genres = str(game['genero']).split(",")
            user_genres = preferences.genre.split(",")
            common_genres = [g for g in user_genres for g2 in genres if g in g2]
            if len(common_genres) > 0:
                score = score + 1

            price = get_clean_price(game['preco'])
            price_interval = get_price_interval(float(price))

            if preferences.price and price_interval == preferences.price:

                score = score + 1

            game['score'] = score

            if score > 0:
                recommended_games[counter] = game
                counter = counter + 1

        # recommended_games = sorted(recommended_games.items(), key=operator.itemgetter(0))
        recommended_games = sorted(recommended_games.items(),
                                  key=lambda kv: kv[1]['score'], reverse=True)
        return recommended_games[:5]

    def get(self, request):
        step = int(request.GET.get('step', 100))
        genres = GENRES_LIST
        games_file = open(os.path.join(settings.BASE_DIR, 'jogos.json'))
        games = json.load(games_file)
        recommended_games = {}
        if UserPreference.objects.filter(user=request.user).count() > 0:
            recommended_games = self.get_recommended(games)
        context = {'games' : games[:step], 'recommended_games' : recommended_games, 'genres': genres}
        return render(request, 'home.html', context)

    def post(self, request):
        platform = request.POST.getlist('platform', [])
        genre = request.POST.getlist('genre', [])
        price = request.POST.get('price', '')

        platform = ','.join(platform)
        genre = ','.join(genre)
        if UserPreference.objects.filter(user=request.user).count() > 0:
            preference = UserPreference.objects.get(user=request.user)
            preference.platform = platform
            preference.genre = genre
            preference.price = price
        else:
            preference = UserPreference(user=request.user, platform=platform, genre=genre, price=price)
        preference.save()
        return HttpResponseRedirect('/')
