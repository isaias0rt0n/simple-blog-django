from django.contrib import admin
from .models import Post

admin.site.register(Post)  # tornar nosso modelo visível na página de administração


