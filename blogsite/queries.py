from blogsite.models import Post
from django.db.models import Q, F, Avg, Count
from django.utils.text import slugify


posts = Post.objects.all() # Retorna un QuerySet con todos los registros de la tabla "Post".

# Posts cuyo autor sea "juan perez"
posts_john = Post.objects.filter(author="juan perez")

# Posts creados después de una fecha específica
from datetime import datetime
fecha = datetime(2021, 1, 1)
posts_recientes = Post.objects.filter(created_on__gt=fecha)

# Excluir los posts escritos por "Admin"
posts_no_admin = Post.objects.exclude(author="Admin")


# Obtener un post con un slug específico
try:
    post_especifico = Post.objects.get(slug="primer-post")
except Post.DoesNotExist:
    post_especifico = None


# Posts cuyo autor sea "John Doe" O que contengan "Django" en el título
posts_condicionales = Post.objects.filter(Q(author="juan perez") | Q(title__icontains="Django"))


# Ordenar los posts por título ascendente
posts_ordenados = Post.objects.all().order_by('title')

# Ordenar por fecha de creación descendente
posts_recientes_primero = Post.objects.all().order_by('-created_on')

# Obtener los primeros 5 posts más recientes
cinco_posts = Post.objects.all().order_by('-created_on')[:5]

# Obtener la fecha promedio de creación (no muy útil, pero ilustrativo)
fecha_promedio = Post.objects.aggregate(promedio=Avg('created_on'))

# Contar cuántos posts ha escrito cada autor
posts_por_autor = Post.objects.values('author').annotate(total=Count('id'))

# Ejemplo más práctico: obtener el total de posts
total_posts = Post.objects.aggregate(total=Count('id'))
print(total_posts['total'])


# Consulta SQL cruda para obtener todos los posts creados por "juan perez"
posts_raw = Post.objects.raw('SELECT * FROM blog_post WHERE author = %s', ['juan perez'])

for p in posts_raw:
    print(p.title, p.author)

