from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=20, verbose_name='Subcategories'),
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name


class TechnicalDoc(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Technical Document'
        verbose_name_plural = 'Technical Documents'

    def __str__(self):
        return str(self.category) + "/" + self.title
