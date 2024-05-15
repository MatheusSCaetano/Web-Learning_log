from django.contrib import admin
from learning_logs.models import Topic,Entry  #Importando de dentro do models a classe Topic que criamos


admin.site.register(Topic) #Registro de Topic
admin.site.register(Entry)

# Register your models here. -> importar model que eu quero que apareça no painel administrativo