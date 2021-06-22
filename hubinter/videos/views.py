from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db import IntegrityError
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView
from django.db.models import Q
from .models import *
from .utils import *
from .forms import AddVideoForm
from delorean import Delorean
import loguru
import uuid


# НАЧАЛ ДЕЛАТЬ САЙТ 10 МАЯ

'''
ЗАДАЧИ:

- АДМИНКА:
	Динамическое отображение нужных тэгов при выборе темы в админке (для Video)
	Доступ к редактированию видео админом

- ВИДЕО:
	Форма добавления видео (ajax-запрос при сабмите, оформление ошибок, flash-сообщение при успешном добавлении)
	Страница видео (DetailView)

- ВЗАИМОДЕЙСТВИЕ:
	Оптимизация SQL-запросов на главной странице
	Авторизация/Регистрация
	Пагинация (где надо)



- ДОДЕЛАТЬ:
	Анимацию фильтрации по тэгам на главной
	Стили для формы добавления видео
'''


# ==================== CLASSES ==================== #

class Home(ListView):
	model = Video
	template_name = 'videos/index.html'
	context_object_name = 'videos'
	queryset = Video.objects.filter(is_published=True).order_by('-created_at')



class SearchVideos(ListView):
	model = Video
	template_name = 'videos/video_search.html'
	context_object_name = 'found_videos'

	def get(self, request, *args, **kwargs):
		if request.GET.get('q').strip():
			queryset = self.get_queryset()
		else:
			return redirect('home')
		return super().get(request, *args, **kwargs)

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.GET.get('q'):
			context['search_query'] = self.request.GET.get('q')
		return context

	def get_queryset(self):
		query = self.request.GET.get('q')
		queryset = self.model.objects.filter( 
			Q(title__icontains=query) | 
			Q(description__icontains=query) | 
			Q(tags__name__icontains=query) |
			Q(theme__name__icontains=query)
		)
		return queryset



class VideoDetail(DetailView):
	model = Video
	template_name = 'videos/video.html'
	context_object_name = 'video'

	def get_queryset(self):
		if self.kwargs['slug']:
			return Video.objects.filter(slug=self.kwargs['slug'])
		else:
			return Video.objects.first()





class AddVideo(CreateView):
	model = Video
	form_class = AddVideoForm
	template_name = "videos/add_video.html"

	def form_valid(self, form):
		self.object = form.save(commit=False)

		self.object.author = self.request.user	
		self.object.slug = slugify(self.object.title)

		try:
			self.object.save()
		except IntegrityError: #add 5 random symbols to slug, if it is not unique
			self.object.slug = slugify(self.object.title) + "_" + str(uuid.uuid4())[:5]
			self.object.save() #and try to save again

		return HttpResponseRedirect(self.get_success_url())





@method_decorator( cache_page(60 * 5), name="dispatch" )
class About(TemplateView):
	template_name = 'about.html'


class Contact(FormView):
	template_name = 'contact.html'
	form_class = About #