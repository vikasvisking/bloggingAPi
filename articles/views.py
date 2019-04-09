from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, BlogSerializer

# for apiview
from rest_framework.views import APIView

# for generic view
from rest_framework.generics import GenericAPIView , CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Create your views here.

#  create api view using CRUD operation CreateReadUpdateDelete

# Using Api View
class ArticleView(APIView):

	def get(self,request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many = True)
		return Response({'articles' : serializer.data})

	def post(self, request):
		article =  request.data.get('article')

		# create article from above data
		serializer = ArticleSerializer(data = article)
		if serializer.is_valid(raise_exception = True):
			article_saved = serializer.save()
		return Response({'successfull' : 'Article "{}" has been successfull created'.format(article_saved.title)})

	def put(self, request, pk):
		saved_article = get_object_or_404(Article, pk = pk)
		data =  request.data.get('article')
		serializer = ArticleSerializer(instance = saved_article, data = data, partial = True)
		if serializer.is_valid(raise_exception = True):
			article_saved = serializer.save()
		return Response({'successfull' : 'Article "{}" has been successfull created'.format(article_saved.title)})

	def delete(self, request, pk):
		article = get_object_or_404(Article, pk = pk)
		article.delete()
		return Response({"message": "Article '{}' has been successfull deleted".format(pk),'status':204})


# Using Genereic View
class BlogView(ListModelMixin, CreateModelMixin, GenericAPIView):
	queryset = Article.objects.all()
	serializer_class = BlogSerializer

	def perform_create(self, serializer):
		author = get_object_or_404(Article, id = self.request.data.get('author_id'))
		return serializer.save(author = author)

	def perform_update(self, serializer):
		author = get_object_or_404(Article, id = self.request.data.get('author_id'))
		return serializer.save(author = author)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self,request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

# CreatAPIVIEW and ListAPI view
class BlogApiView(CreateAPIView, ListAPIView):
	queryset = Article.objects.all()
	serializer_class = BlogSerializer

	def perform_create(self, serializer):
		author = get_object_or_404(Article, id = self.request.data.get('author_id'))
		return serializer.save(author =author)

# list create api view
class BlogListCreate(ListCreateAPIView):
	queryset = Article.objects.all()
	serializer_class = BlogSerializer

	def perform_create(self, serializer):
		author = get_object_or_404(Author, id = self.request.date.get('author_id'))
		return serializer.save(author = author)

# update single blog post
class SingleArticleView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# list single article
# class SingleArticleView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# list update delete:
class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer