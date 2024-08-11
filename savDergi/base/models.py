from django.db import models
from django.utils.text import slugify


class Duyuru(models.Model):

    BLOCK_TYPES = (
        ('paragraph', 'Paragraph'),
        ('image', 'Image')
    )

    topic = models.CharField(max_length=200)

    block_type = models.CharField(max_length=10, choices=BLOCK_TYPES, default='')
    text = models.TextField(blank=True, null=True)  # For paragraph text
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # For images
    order = models.PositiveIntegerField(default=0)  # To maintain the order of blocks

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
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.get_block_type_display()} -{str(self.order)}"


class Album(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.image)

