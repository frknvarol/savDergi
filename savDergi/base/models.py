from django.db import models
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


class AlbumImage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.ForeignKey(Album, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.image)


class Sayi(models.Model):
    sayi = models.IntegerField(unique=True, default=0, blank=False)

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
    baslik = models.CharField(max_length=100, default='baslik')
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
            base_slug = slugify(self.baslik)
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
        return f"makale başlığı: {self.baslik}"


class MakaleKaynak(models.Model):
    baslik = models.ForeignKey(Makale, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    kaynak = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"kaynak :{self.kaynak}"


class MakaleAnahtar(models.Model):
    baslik = models.ForeignKey(Makale, on_delete=models.CASCADE)
    anahtar = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"anahtar :{self.anahtar} "


class MakaleYazar(models.Model):
    baslik = models.ForeignKey(Makale, on_delete=models.CASCADE)
    yazar = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"yazar: {self.yazar} "


class Portre(models.Model):
    baslik = models.CharField(max_length=100, blank=False, null=False, default="Başlık")
    roportaj = models.TextField(blank=False, null=False, default="röportaj", max_length=99999)
    link = models.URLField(blank=False, null=False, default="https://open.spotify.com/show/2HE4WPETsojDxh9GRFIiZP?si=8cf043f5e13d41bb")
    oz_gecmis = models.TextField(blank=False, null=False, default="öz geçmiş", max_length=99999)
    oz_gecmis_img = models.ImageField(blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.baslik)
            slug = base_slug
            counter = 1

            while Portre.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Portre, self).save(*args, **kwargs)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.baslik}"


class Konferans(models.Model):
    baslik = models.CharField(max_length=100, blank=False, null=False, default="Başlık")
    text = models.TextField(blank=False, null=False, default="konferans text", max_length=99999)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.baslik)
            slug = base_slug
            counter = 1

            while Konferans.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Konferans, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Konferans: {self.baslik}"


class KonferansImage(models.Model):
    baslik = models.ForeignKey(Konferans, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.baslik} image"


class Metodoloji(models.Model):
    baslik = models.CharField(max_length=100, blank=False, null=False, default="Metodoloji başlık")
    text = models.TextField(blank=False, null=False, default="metodoloji text", max_length=99999)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.baslik)
            slug = base_slug
            counter = 1

            while Metodoloji.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Metodoloji, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Metodoloji: {self.baslik}"


class MetodolojiImage(models.Model):
    baslik = models.ForeignKey(Metodoloji, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.baslik} image"


class Sava(models.Model):
    baslik = models.CharField(max_length=100, blank=False, null=False, default="SAVA başlık")
    text = models.TextField(blank=False, null=False, default="SAVA text", max_length=99999)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.baslik)
            slug = base_slug
            counter = 1

            while Sava.objects.filter(slug=slug):
                slug = f"{slug}-{counter}"
                counter += 1

            self.slug = slug

        super(Sava, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"SAVA: {self.baslik}"


class SavaImage(models.Model):
    baslik = models.ForeignKey(Sava, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.baslik} image"