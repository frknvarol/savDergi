from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField


class Duyuru(models.Model):

    topic = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.topic)
            slug = base_slug
            counter = 1

            while Duyuru.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Duyuru, self).save(*args, **kwargs)

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

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Album.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Album, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-updated', '-created', ]

    slug = models.SlugField(editable=False, unique=True, default=slugify('name'))

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Album.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Album, self).save(*args, **kwargs)

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


class Sayi(models.Model):
    sayi = models.IntegerField(max_length=100, unique=True, default=0, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.sayi)
            slug = base_slug
            counter = 1

            while Sayi.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Sayi, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"sayi: {self.sayi}"


class Makale(models.Model):
    konu = models.CharField(max_length=100, default='konu')
    Oz = models.TextField(max_length=10000, default='Öz')
    bolum = models.CharField(max_length=100, default='bölüm')
    birinci_dil = models.CharField(max_length=100, default='birinci dil')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sayi = models.ForeignKey(Sayi, on_delete=models.CASCADE)

    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True,)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.konu)
            slug = base_slug
            counter = 1

            while Makale.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Makale, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"makale: {self.konu}"


class MakaleText(models.Model):
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.konu} paragraf"


class MakaleKaynak(models.Model):
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    kaynak = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"kaynak :{self.kaynak}"


class MakaleAnahtar(models.Model):
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    anahtar = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"anahtar :{self.anahtar} "


class MakaleYazar(models.Model):
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    yazar = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"yazar: {self.yazar} "
