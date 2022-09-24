from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "Main/home.html"
    extra_context = {"title_name": "Главная страница"}