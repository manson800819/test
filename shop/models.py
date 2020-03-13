from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True
                            ,default=False)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # print("get_c", [self.slug])
        return reverse('shop:product_list_by_category',
                       args=[self.slug])
class Type1(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)

    print(1)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('shop:product_tpy',
                       args=[self.id,self.slug])


class Product(models.Model):
    type1 = models.ForeignKey(Type1,
                                 related_name='products_t')
    category = models.ForeignKey(Category,
                                 related_name='products_c'
                                 ,default=False)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=False)
    # 台灣價錢都是整數，所以可以設定 decimal_places=0
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.available,self.slug])
