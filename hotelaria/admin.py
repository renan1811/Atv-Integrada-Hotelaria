from django.contrib import admin
from .models import Hospede, Serviço, Pagamento

admin.site.register(Hospede)
admin.site.register(Serviço)
admin.site.register(Pagamento)
