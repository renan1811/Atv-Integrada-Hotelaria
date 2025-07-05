from django.contrib import admin
from .models import Hospede, Serviço, Pagamento, Quarto, Funcionario

admin.site.register(Hospede)
admin.site.register(Serviço)
admin.site.register(Pagamento)
admin.site.register(Quarto)
admin.site.register(Funcionario)
