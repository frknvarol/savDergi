from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField


class Duyuru(models.Model):

    topic = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, blank=True)

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

    slug = models.SlugField(unique=True, blank=True)

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
    sayi = models.CharField(max_length=100, unique=True, default=1, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, blank=True)

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

    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.konu}"


class MakaleText(models.Model):
    sayi = models.ForeignKey(Makale, on_delete=models.CASCADE)
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.topic} paragraf"


class MakaleKaynak(models.Model):
    sayi = models.ForeignKey(Makale, on_delete=models.CASCADE)
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    kaynak = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.kaynak}"


class MakaleAnahtar(models.Model):
    sayi = models.ForeignKey(Makale, on_delete=models.CASCADE)
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    anahtar = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.anahtar} "


class MakaleYazar(models.Model):
    sayi = models.ForeignKey(Makale, on_delete=models.CASCADE)
    konu = models.ForeignKey(Makale, on_delete=models.CASCADE)
    yazar = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.yazar} "


# Slug functions

@receiver(pre_save, sender=Album)
def generate_unique_slug(sender, instance, **kwargs):
    if not instance.slug or instance.name != sender.objects.filter(pk=instance.pk).first().name:
        base_slug = slugify(instance.name)
        slug = base_slug
        counter = 1

        while sender.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug


@receiver(pre_save, sender=Duyuru)
def generate_unique_slug(sender, instance, **kwargs):
    if not instance.slug or instance.topic != sender.objects.filter(pk=instance.pk).first().topic:
        base_slug = slugify(instance.topic)
        slug = base_slug
        counter = 1

        while sender.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug


@receiver(pre_save, sender=Makale)
def generate_unique_slug(sender, instance, **kwargs):
    if not instance.slug or instance.konu != sender.objects.filter(pk=instance.pk).first().konu:
        base_slug = slugify(instance.konu)
        slug = base_slug
        counter = 1

        while sender.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug


@receiver(pre_save, sender=Sayi)
def generate_unique_slug(sender, instance, **kwargs):
    if not instance.slug or instance.sayi != sender.objects.filter(pk=instance.pk).first().sayi:
        base_slug = slugify(instance.sayi)
        slug = base_slug
        counter = 1

        while sender.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug