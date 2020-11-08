from django.db import models

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
