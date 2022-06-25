from django.urls import URLPattern, path

URLPattern = path("blog/", include("blog.urls", namespace="blog"))