from django.db import models
import uuid

class Survey(models.Model):

    name = models.CharField('Araştırma Adı', max_length=100)
    active = models.BooleanField('Aktif mi?', null=False, blank=False, default=False)
    created_at = models.DateTimeField('Oluşturulma Tarihi', null=True, blank=True, auto_now=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', null=True, blank=True, auto_now_add=True)

    class Meta:

        verbose_name = 'Araştırma'
        verbose_name_plural = 'Araştırmalar'

    def __str__(self):
        return str(self.name)

class Soru(models.Model):

    survey = models.ForeignKey(Survey, verbose_name='Araştırma', null=False, blank=False)
    baslik = models.CharField('Başlık', max_length=40)
    soru = models.TextField('Soru', blank=True, null=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField('Sorulma Tarihi', null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'

    def __str__(self):
        return str(self.baslik)
