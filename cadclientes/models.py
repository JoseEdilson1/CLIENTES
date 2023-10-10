from django.db import models

# Create your models here.

class Cliente(models.Model):
    
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(default="1980-01-01")
    email = models.EmailField()
    idade = models.PositiveSmallIntegerField()
    cpf = models.CharField(max_length=11, blank=True, null=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"