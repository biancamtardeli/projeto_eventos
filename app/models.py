from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome_categoria
    

class UF(models.Model):
    uf = models.CharField(max_length=2, default='')

    class Meta:
        verbose_name_plural = "UFs"

    def __str__(self):
        return self.uf
    

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100, default='')
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome_cidade
    

class MeioDivulgacao(models.Model):
    meio_divulgacao = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name_plural = "Meios de Divulgação"
        
    def __str__(self):
        return self.meio_divulgacao
    

class Publico(models.Model):
    publico = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name_plural = "Públicos"
        
    def __str__(self):
        return self.publico
    

class Local(models.Model):
    nome_local = models.CharField(max_length=100, default='')
    capacidade = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Locais"
        
    def __str__(self):
        return f'{self.nome_local}'
    

class Material(models.Model):
    nome_material= models.CharField(max_length=100, default='')
    qtd = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Materiais"
        
    def __str__(self):
        return f'{self.nome_material}'
    

class TipoParceria(models.Model):
    tipo_parceria = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name_plural = "Tipos de Parceria"
        
    def __str__(self):
        return f'{self.tipo_parceria}'
    

class Parceria(models.Model):
    nome_parceiro = models.CharField(max_length=100, default='')
    tipo_parceria = models.ForeignKey(TipoParceria, on_delete=models.CASCADE, default='')
    descricao = models.CharField(max_length=150, default='')

    class Meta:
        verbose_name_plural = "Parcerias"
        
    def __str__(self):
        return f'{self.nome_parceiro}'
    

class Colaborador(models.Model):
    nome_colaborador = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=50, default='')
    telefone = models.CharField(max_length=13, default='')
    cargo = models.CharField(max_length=50, default='')
    

    class Meta:
        verbose_name_plural = "Colaboradores"
        
    def __str__(self):
        return f'{self.nome_colaborador}'
    

class TipoCobertura(models.Model):
    tipo_cobertura = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name_plural = "Tipos de Cobertura"
        
    def __str__(self):
        return f'{self.tipo_cobertura}'
    

class Cobertura(models.Model):
    cobertura_colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, default='')
    tipo_cobertura = models.ForeignKey(TipoCobertura, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name_plural = "Coberturas"

    def __str__(self):
        return self.cobertura_colaborador
    

class Organizador(models.Model):
    nome_organizador = models.CharField(max_length=100, default='')
    instituicao = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=50, default='')
    telefone = models.CharField(max_length=13, default='')

    class Meta:
        verbose_name_plural = "Organizadores"
        
    def __str__(self):
        return f'{self.nome_organizador}'
    
class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=100, default='')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name_plural = "instituições"
        
    def __str__(self):
        return f'{self.nome_instituicao}'
    
class Divulgacao(models.Model):
    cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE, default='')
    divulgacao = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name_plural = "Divulgações"
        
    def __str__(self):
        return self.meio_divulgacao


class Evento(models.Model):
    nome_evento = models.CharField(max_length=100, default='')
    data_evento = models.DateField(default='2000-01-01')
    horario_inicio = models.TimeField(default='00:00:00')
    horario_fim = models.TimeField(default='00:00:00')
    descricao = models.CharField(max_length=150, default='')
    qtd_publico = models.IntegerField(default=0)
    publico = models.ForeignKey(Publico, on_delete=models.CASCADE, default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='')
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, default='')
    local = models.ForeignKey(Local, on_delete=models.CASCADE, default='')
    cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE, default='')
    parceria = models.ForeignKey(Parceria, on_delete=models.CASCADE, default='')
    material = models.ManyToManyField(Material, default='')

    class Meta:
        verbose_name_plural = "Eventos"
        
    def __str__(self):
        return f'{self.nome_evento}'