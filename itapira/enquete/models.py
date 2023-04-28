from django.db import models

# Create your models here.
class Questao(models.Model):
    pergunta = models.CharField(max_length=200)
    data= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pergunta} - {self.data}" 


class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.resposta