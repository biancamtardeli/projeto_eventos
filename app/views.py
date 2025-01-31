from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
      page = "index.html"
      context = {
        "categorias": Categoria.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class CategoriaView(View):
    def get(self, request):
      page = "categoria.html"
      context = {
        "categorias": Categoria.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class UFView(View):
    def get(self, request):
      page = "uf.html"
      context = {
        "ufs": UF.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class CidadeView(View):
    def get(self, request):
      page = "cidade.html"
      context = {
        "cidades": Cidade.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class InstituicaoView(View):
    def get(self, request):
      page = "instituicao.html"
      context = {
        "instituicoes": Instituicao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class MeioDivulgacaoView(View):
    def get(self, request):
      page = "meioDivulgacao.html"
      context = {
        "meiosDivulgacao": MeioDivulgacao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class PublicoView(View):
    def get(self, request):
      page = "publico.html"
      context = {
        "publicos": Publico.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class LocalView(View):
    def get(self, request):
      page = "local.html"
      context = {
        "locais": Local.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class MaterialView(View):
    def get(self, request):
      page = "material.html"
      context = {
        "materiais": Material.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class ParceriaView(View):
    def get(self, request):
      page = "parceria.html"
      context = {
        "parcerias": Parceria.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class CoberturaView(View):
    def get(self, request):
      page = "cobertura.html"
      context = {
        "coberturas": Cobertura.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class OrganizadorView(View):
    def get(self, request):
      page = "organizador.html"
      context = {
        "organizadores": Organizador.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class EventoView(View):
    def get(self, request):
      page = "evento.html"
      context = {
        "eventos": Evento.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class ColaboradorView(View):
    def get(self, request):
      page = "colaborador.html"
      context = {
        "colaboradores": Colaborador.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class TipoCoberturaView(View):
    def get(self, request):
      page = "tipoCobertura.html"
      context = {
        "tiposCobertura": TipoCobertura.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class TipoParceriaView(View):
    def get(self, request):
      page = "tipoParceria.html"
      context = {
        "tiposParceria": TipoParceria.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class DivulgacaoView(View):
    def get(self, request):
      page = "divulgacao.html"
      context = {
        "divulgacoes": Divulgacao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass