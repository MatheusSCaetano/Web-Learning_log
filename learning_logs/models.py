from django.db import models

# Create your models here. manipular o basnco de dados

class Topic(models.Model): # a classe será uma tabela no banco de dados -> Topico <-
    """Um assunto sobre o qual o usuario está aprendendo"""
    text = models.CharField(max_length=200) #campo do tipo texto 
    date_added = models.DateTimeField(auto_now_add=True) # automaticamente preenchar data e horario do registro do topic

    def __str__(self):
        """Devolve uma reperesentacao em string do modelo."""
        return self.text
    
class Entry(models.Model):
    """Algo específico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # "Foringkey" -> chave estrangeira -> cada entrada está relaciodada a um topico, logo deve-se usar a chave estrangeira para haver a correlação
# A utilização do "on_delete" é obrigatória -> o tipo CASCADE deleta em cascata as entradas, caso o topico seja excluido -> CASCADE é apenas um dos varios tipos de on_delete;
    text = models.TextField() # nesse "TextField" nao expecificamos o numero de caracteres para que seja de livre arbitrio do user
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries' # -> apenas para quando o django for utilizar o plural de entry

    def __str__(self):
            """Devolve uma representação em string do modelo"""
            return self.text[:50] + '...' # -> apresenta os primeiros 50 caracteres, caso tenha mais ficara a  + "..."