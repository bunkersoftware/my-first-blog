#from django.db import models

from django.db import models
from django.utils import timezone

# definicao da classe e das propriedades da classe
# models.Model informa que Post eh um modelo django e que deve ser gravado no banco de dados
# charfield para campos com limite de caracteres, textfield para campos sem limites
# foreignkey eh um link para outro modelo

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

# metodos da classe

def publish(self):
    self.published_date = timezone.now()
    self.save()

# obs: __ e chamado de dunder (double-underscore) frequentemente usado em python
def __str__(self):
    return self.title
