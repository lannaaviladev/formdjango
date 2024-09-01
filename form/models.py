from django.db import models

# Create your models here.


LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')

]

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    data_nascimento= models.DateTimeField()
    sexo = models.CharField(max_length=150,choices= LISTA_SEXO)

    def __str__(self) -> str:
        return self.nome