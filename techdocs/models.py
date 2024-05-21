from django.db import models


# Create your models here.
class Supercategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Supercategory'
        verbose_name_plural = 'Supercategories'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    parent = models.ForeignKey('Supercategory', null=True, blank=True, related_name='child_category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        unique_together = ('parent', 'slug')

    def __str__(self):
        if self.parent is None:
            return str(self.name)
        else:
            return str(self.parent) + " / " + self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=20, default="EMPTY")
    description = models.CharField(max_length=100)
    parent = models.ForeignKey('Category', null=True, blank=True, related_name='child_subcategory', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        unique_together = ('parent', 'slug')

    def __str__(self):
        return self.name


class TechnicalDoc(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Technical Document'
        verbose_name_plural = 'Technical Documents'
        unique_together = ('category', 'slug')

    def __str__(self):
        return str(self.category) + "/" + self.title
