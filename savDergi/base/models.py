from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField


class Duyuru(models.Model):

    topic = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(editable=False, unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         base_slug = slugify(self.topic)
    #         slug = base_slug
    #         counter = 1
    #
    #         while Duyuru.objects.filter(slug=slug):
    #             slug = f"{slug}-{counter}"
    #             counter += 1
    #
    #         self.slug = slug
    #
    #     super(Duyuru, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-updated', '-created',]

    def __str__(self):
        return self.topic


class DuyuruText(models.Model):
    text = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Duyuru, on_delete=models.CASCADE)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.topic} text"


class DuyuruImage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Duyuru, on_delete=models.CASCADE)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.topic} image"


class Album(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(editable=False, unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         base_slug = slugify(self.name)
    #         slug = base_slug
    #         counter = 1
    #
    #         while Album.objects.filter(slug=slug):
    #             slug = f"{slug}-{counter}"
    #             counter += 1
    #
    #         self.slug = slug
    #
    #     super(Album, self).save(*args, **kwargs)
    #

    class Meta:
        ordering = ['-updated', '-created', ]

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.ForeignKey(Album, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.image)


class EmbeddedVideo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = EmbedVideoField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Dergi(models.Model):
    topic = models.CharField(max_length=100, default='makale')
    konu = models.CharField(max_length=100, default='konu')
    Oz = models.TextField(max_length=10000, default='Öz')
    bolum = models.CharField(max_length=100, default='bölüm')
    birinci_dil = models.CharField(max_length=100, default='birinci dil')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sayi = models.IntegerField(default=1, unique=True)

    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True,)

    slug = models.SlugField(editable=False, unique=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.topic}"


class DergiText(models.Model):
    topic = models.ForeignKey(Dergi, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.topic} paragraf"


class DergiKaynak(models.Model):
    topic = models.ForeignKey(Dergi, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    kaynak = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.kaynak}"


class DergiAnahtar(models.Model):
    topic = models.ForeignKey(Dergi, on_delete=models.CASCADE)
    anahtar = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.anahtar} "


class DergiYazar(models.Model):
    topic = models.ForeignKey(Dergi, on_delete=models.CASCADE)
    yazar = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.yazar} "


@receiver(pre_save, sender=Album)
def generate_unique_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.name)
        slug = base_slug
        counter = 1

        while sender.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug


@receiver(pre_save, sender=Duyuru)
def generate_unique_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.topic)
        slug = base_slug
        counter = 1

        while sender.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug


@receiver(pre_save, sender=Dergi)
def generate_unique_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.topic)
        slug = base_slug
        counter = 1

        while sender.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug
