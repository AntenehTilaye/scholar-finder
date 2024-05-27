from django.urls import path
from . import views

urlpatterns = [
    path("author/publications-google/<str:name>",views.getAuthorPublications, name="publication-of-author"),
    path("author/publications-google/<str:name>/<int:year>",views.getAuthorPublicationsByYear, name="publication-of-author-by-year"),
    
    path("author/publications-sematic/<str:name>",views.getAuthorPublicationsSemantic, name="publication-of-author"),
    path("author/publications-sematic/<str:name>/<int:year>",views.getAuthorPublicationsSemanticByYear, name="publication-of-author"),

    path("author/publications/<str:name>",views.getAuthorPublicationsBoth, name="publication-of-author"),
    path("author/publications/<str:name>/<int:year>",views.getAuthorPublicationsBothByYear, name="publication-of-author"),

    
]
