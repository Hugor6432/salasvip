from django.db import models


class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome} ({self.capacidade} pessoas)"
    
    class Meta:
        verbose_name_plural = "Salas"


class Recurso(models.Model):
    TIPOS = [
        ('projetor', 'Projetor'),
        ('wifi', 'WiFi'),
        ('tv', 'TV'),
        ('whiteboard', 'Quadro Branco'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='recursos')
    
    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"


class Recorrencia(models.Model):
    FREQUENCIAS = [
        ('unica', 'Única'),
        ('diaria', 'Diária'),
        ('semanal', 'Semanal'),
        ('mensal', 'Mensal'),
    ]
    
    frequencia = models.CharField(max_length=20, choices=FREQUENCIAS)
    
    def __str__(self):
        return self.get_frequencia_display()


class Reserva(models.Model):
    STATUSOS = [
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='reservas')
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    responsavel = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    recorrencia = models.ForeignKey(Recorrencia, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSOS, default='pendente')
    
    def __str__(self):
        return f"{self.sala.nome} - {self.data_inicio.strftime('%d/%m/%Y %H:%M')}"
    
    def tem_conflito(self):
        conflitantes = Reserva.objects.filter(
            sala=self.sala,
            status__in=['confirmada', 'pendente']
        ).exclude(id=self.id)
        
        for reserva in conflitantes:
            if not (self.data_fim <= reserva.data_inicio or self.data_inicio >= reserva.data_fim):
                return True
        return False
    
    class Meta:
        verbose_name_plural = "Reservas"
        ordering = ['-data_inicio']
