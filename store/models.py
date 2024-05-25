from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class DateTime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DateTime):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='category/', default=None)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'Category'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
