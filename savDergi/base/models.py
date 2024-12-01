from django.db import models
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField


class Duyuru(models.Model):

    topic = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(editable=False, unique=True, default=slugify('topic'))

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


class Dergi(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    author = models.TextField(blank=False, null=False)


class DergiMakale(models.Model):
    title = models.ForeignKey(Dergi, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.title} makale"


class DergiMakaleText(models.Model):
    title = models.ForeignKey(DergiMakale, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.title} makale"


class DergiSource(models.Model):
    title = models.ForeignKey(Dergi, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    source = models.TextField(blank=False, null=False)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.source}"


class DergiKeyword(models.Model):
    title = models.ForeignKey(Dergi, on_delete=models.CASCADE)
    keyword = models.TextField()
    ordering = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.keyword} "
