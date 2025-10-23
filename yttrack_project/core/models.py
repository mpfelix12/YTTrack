from django.db import models
from django.urls import reverse

class Quadro(models.Model):
    nome = models.CharField('Nome do Quadro', max_length=200)
    cover_color = models.CharField('Cor/Gradiente', max_length=120, default='#ff7a7a')
    descricao = models.TextField('Descrição', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('core:videos_por_quadro', args=[self.pk])


class Video(models.Model):
    quadro = models.ForeignKey(Quadro, related_name='videos', on_delete=models.CASCADE)
    titulo = models.CharField('Título do vídeo', max_length=200)
    descricao = models.TextField('Descrição', blank=True)
    video_arquivo = models.FileField(upload_to='videos/', blank=True, null=True)
    video_link = models.URLField('Link do YouTube', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    watched = models.BooleanField('Assistido', default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

    def get_video_url(self):
        """Retorna o link para o player, seja YouTube ou arquivo local"""
        if self.video_link:
            # transforma link do YouTube em embed
            if "youtube.com/watch" in self.video_link:
                video_id = self.video_link.split("v=")[-1]
                return f"https://www.youtube.com/embed/{video_id}"
            elif "youtu.be/" in self.video_link:
                video_id = self.video_link.split("youtu.be/")[-1]
                return f"https://www.youtube.com/embed/{video_id}"
            return self.video_link
        elif self.video_arquivo:
            return self.video_arquivo.url
        return ""
