from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Musician, Album
from django.shortcuts import render, redirect
from .models import Musician, Album
from .forms import AddSongForm , AddSingerForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render
 
class IndexView(generic.ListView):
    template_name = 'artisr/index.html'
    context_object_name = 'singers'
    def get_queryset(self):
        return Musician.objects.all()
class DetailView(generic.DetailView):
    model = Musician
    template_name = 'artisr/detail.html'
class ResultsView(generic.DetailView):
    model = Musician
    template_name = 'artisr/results.html'       
@login_required(login_url='artisr:user_login')
def delete_song(request, musician_id):
    song = get_object_or_404(Album, pk=musician_id)
    song.delete()
    return redirect('artisr:results', song.artist_id)
@login_required(login_url='artisr:user_login')
def num_stars_function(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    if request.method == 'POST':
        try:
            num_stars_list = []
            for song in musician.album_set.all():
                selected_song = musician.album_set.get(pk=request.POST.get(f'song_{song.id}'))
                num_stars = int(request.POST.get(f'num_stars_{song.id}'))
                num_stars_list.append(num_stars)
                selected_song.num_stars = num_stars
                selected_song.save()
            if len(num_stars_list) != len(set(num_stars_list)):
                return render(request, 'artisr/detail.html', {
                    'musician': musician,
                    'error_messsage': "SỐ THỨ TỰ KHÔNG ĐƯỢC TRÙNG NHAU",
                })              
        except (KeyError, Album.DoesNotExist):
            return render(request, 'artisr/detail.html', {
                'musician': musician,
                'error_message': "You didn't select a choice.",
            })
        else:          
            return HttpResponseRedirect(reverse('artisr:results', args=(musician.id,))+ f'?num_stars={num_stars}')
    else:
        return HttpResponseRedirect(reverse('artisr:results', args=(musician.id,)))
@login_required(login_url='artisr:user_login')
def add_song(request, musician_id):
    musician = Musician.objects.get(pk=musician_id)
    if request.method == 'POST':   
        form = AddSongForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data['name']
            release_date1 = form.cleaned_data['release_date']
            num_stars1 = form.cleaned_data['num_stars']
            song_lyrics1 = form.cleaned_data['song_lyrics']
            if int(num_stars1)<=0:
                return render(request, 'artisr/add_song.html', {
                    'musician': musician,
                    'form': form,
                    'error_messsage': "SỐ THỨ TỰ KHÔNG ĐƯỢC NHỎ HƠN 0",}) 
            if musician.album_set.filter(num_stars=num_stars1).exists():
                    return render(request, 'artisr/add_song.html', {
                        'musician': musician,
                        'form': form,
                        'error_messsage': "SỐ THỨ TỰ ĐÃ TỒN TẠI",
                    })    
            album = Album(artist_id=musician_id, name=name1, release_date=release_date1, num_stars=num_stars1, song_lyrics= song_lyrics1)  
            album.save()
            return redirect(reverse('artisr:results', args=(musician.id,)))            
    else:
        form = AddSongForm()
    all_musicians = Musician.objects.all()
    return render(request, 'artisr/add_song.html', {'form': form, 'musician': musician,'all_musicians': all_musicians})
def detail_infor(request, musician_id): 
    song = get_object_or_404(Album, pk=musician_id)
    return render(request, 'artisr/detail_infor.html', {'song': song})

@login_required(login_url='artisr:user_login')
def update_infor(request, musician_id):
    album = Album.objects.get(pk=musician_id)
    if request.method == 'POST':    
        if 'update' in request.POST:
            album.name = request.POST['name']
            album.release_date = request.POST['release_date']
            album.num_stars = request.POST['num_stars']
            album.song_lyrics = request.POST['song_lyrics']
            album.save()
            return redirect('artisr:detail_infor', musician_id = musician_id)
    return render(request, 'detail_infor.html' , {'album': album})
    
@login_required(login_url='artisr:user_login')
def delete_singer(request, musician_id):
    singer = get_object_or_404(Musician, pk=musician_id)
    singer.delete()
    return HttpResponseRedirect(reverse('artisr:index'))
@login_required(login_url='artisr:user_login')
def add_singer(request):
    if request.method == 'POST':   
        form = AddSingerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            instrument= form.cleaned_data['instrument']  
            if Musician.objects.filter(first_name=first_name).exists():
                    return render(request, 'artisr/index.html', {
                        'error1': "Tên ca sĩ đã tồn tại! ",
                    })    
            singer = Musician.objects.create(first_name=first_name, last_name=last_name, instrument=instrument)  
            singer.save()
            return redirect('artisr:index')            
    else:              
        form = AddSingerForm()       
    return redirect('artisr:index')   
def search_singer(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        show_form = True
        if query:
            # index_view = IndexView()
            # index_view.request = request
            # index_view.template_name = 'artisr/index.html'
            # index_view.context_object_name = 'singers'
            # singers = index_view.get_queryset().filter(first_name__icontains=query)
            singers = Musician.objects.filter(first_name__icontains=query)
            if not singers: 
                return render(request, 'artisr/index.html', {
                        'error2': "Không tìm thấy tên ca sỹ! ",
                    }) 
        else:
            # index_view = IndexView()
            # index_view.request = request
            # index_view.template_name = 'artisr/index.html'
            # index_view.context_object_name = 'singers'
            # singers = index_view.get_queryset()
            singers = Musician.objects.all()
        context = {'singers': singers, 'show_form': show_form}
        return render(request, 'artisr/index.html', context)
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artisr:index')
    else:
        form = UserCreationForm()
    return render(request, 'artisr/signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            request.session['username'] = user.username
            return redirect('artisr:index')
    else:
        form = AuthenticationForm()
    return render(request, 'artisr/login.html', {'form': form})
def user_logout(request):
    del request.session['username']
    auth_logout(request)
    return redirect('artisr:index')

