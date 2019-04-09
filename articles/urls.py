
from .views import ArticleView, BlogView, BlogApiView, BlogListCreate, SingleArticleView
from django.urls import path

app_name = 'articles'

urlpatterns = [

   # API View
	path('articles/', ArticleView.as_view()),
	path('articles/<int:pk>/', ArticleView.as_view()),

	# Generic View
	path('blogs/', BlogView.as_view()),

	# Create & ListAPi view
	path('blogAPI/', BlogApiView.as_view()),

	# ListCreateApiView
	path('bloglistcreate/', BlogListCreate.as_view()),
	path('bloger/<int:pk>/', SingleArticleView.as_view())

]