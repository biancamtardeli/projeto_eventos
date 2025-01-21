from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome_categoria
    

class TipoDivulgacao(models.Model):
    tipo_divulgacao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tipos de Divulgação"
        
    def __str__(self):
        return self.tipo_divulgacao
    

class MeioDivulgacao(models.Model):
    meio_divulgacao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Meios de Divulgação"
        
    def __str__(self):
        return self.meio_divulgacao
    

class Publico(models.Model):
    publico = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Públicos"
        
    def __str__(self):
        return self.publico
    

class Local(models.Model):
    nome_local = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    class Meta:
        verbose_name_plural = "Locais"
        
    def __str__(self):
        return f'{self.nome_local}'
    

class Material(models.Model):
    nome_material= models.CharField(max_length=100)
    qtd = models.IntegerField()

    class Meta:
        verbose_name_plural = "Materiais"
        
    def __str__(self):
        return f'{self.nome_material}'
    

class Parceria(models.Model):
    nome_parceiro = models.CharField(max_length=100)
    tipo_parceria = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Parcerias"
        
    def __str__(self):
        return f'{self.nome_parceiro}'
    

class Cobertura(models.Model):
    nome_colaborador = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=13)
    cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Coberturas"
        
    def __str__(self):
        return f'{self.nome_colaborador}'
    

class Organizador(models.Model):
    nome_organizador = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=13)

    class Meta:
        verbose_name_plural = "Organizadores"
        
    def __str__(self):
        return f'{self.nome_organizador}'


class Evento(models.Model):
    nome_evento = models.CharField(max_length=100)
    data_evento = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    descricao = models.CharField(max_length=150)
    qtd_publico = models.IntegerField()
    publico = models.ForeignKey(Publico, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE)
    parceria = models.ForeignKey(Parceria, on_delete=models.CASCADE)
    material = models.ManyToManyField(Material, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Eventos"
        
    def __str__(self):
        return f'{self.nome_evento}'