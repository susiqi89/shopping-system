from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class shop_admin(models.Model):
    username = models.CharField(max_length=20, null=True,unique=bool, verbose_name='管理员名称')
    password = models.CharField(max_length=32, null=True, verbose_name='密码')
    email = models.EmailField(max_length=50, null=True, verbose_name='邮箱')

    class Meta:
        verbose_name = u'管理员表'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

class shop_user(models.Model):
    username = models.CharField(max_length=20, null=True, verbose_name=u'用户名')
    password = models.CharField(max_length=32, null=True, verbose_name=u'密码')
    sex = models.BooleanField(max_length=1, choices=((0,'男'),(1,'女'),(2,'保密')), default=2)
    email = models.EmailField(max_length=50, null=True, verbose_name=u'邮箱')
    face = models.ImageField(max_length=50, upload_to='user/', verbose_name=u'用户头像')
    regTime = models.DateField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'用户表'
        verbose_name_plural = verbose_name
        ordering = ['-id']


    def __unicode__(self):
        return self.username

class shop_cat(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'分类名称')
    proname = models.CharField(max_length=50, verbose_name=u'商品小分类', null=True)

    # 网站中用于链接，SlugField自动根据前面内容自动生成英文字母，不支持中文
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=50, unique=True,
        help_text='根据name生成的，用于生成页面URL，必须唯一'
    )
    desc = models.TextField(verbose_name=u'名称描述')
    is_active = models.BooleanField(default=True, verbose_name=u'是否激活（当前分类是否可用）')
    meta_keywords = models.CharField(max_length=255, verbose_name=u'Meta关键词', help_text='meta关键词，有利于SEO，用逗号分割')
    meta_desc = models.CharField(max_length=255, verbose_name=u'Meta描述', help_text='meta描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    # 定义当前models的其他属性
    class Meta:
        db_table = 'categories'
        ordering = ['-proname','name']
        verbose_name_plural = u'分类表'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_app_category', args=(self.slug))


class shop_pro(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'商品名称', unique=True)
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=255, unique=True,
        help_text='根据name生成的，用于生成页面URL，必须唯一'
    )
    brand = models.CharField(max_length=50, verbose_name=u'品牌')
    sku = models.CharField(max_length=50, verbose_name=u'计量单位')
    # max_digits最大用多少位来存储数字，decimal_places小数位数
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'现价')
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00, verbose_name=u'原价')
    image = models.ImageField(max_length=50, upload_to='products/', verbose_name=u'图片')
    is_active = models.BooleanField(default=True, verbose_name=u'设为激活')
    is_bestseller = models.BooleanField(default=False, verbose_name=u'标为热销')
    is_featured = models.BooleanField(default=False, verbose_name=u'标为推荐')
    quantity = models.IntegerField(verbose_name=u'商品数量')
    desc = models.TextField(verbose_name=u'商品描述')
    meta_keywords = models.CharField(
        verbose_name=u'Meta关键词',
        max_length=255, help_text='meta关键词标签，逗号分隔'
    )
    meta_desc = models.CharField(
        verbose_name=u'Meta描述',
        max_length=255, help_text='meta描述标签'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    categories = models.ManyToManyField(shop_cat)

    class Meta:
        db_table = 'shop_pro'
        verbose_name_plural = u'商品表'
        ordering = ['-created_at']

#购物车模型，一种商品可以有多个
class CarItem(models.Model):
    car_id = models.CharField(max_length=50, verbose_name=u'购物车编号')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=u'购物车中商品创建时间')
    quantity = models.IntegerField(default=1,verbose_name=u'数量')
    product = models.ForeignKey('shop_pro', unique=False)

    class Meta:
        db_table = 'car_items'
        verbose_name_plural = u'购物车'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告标题')
    description = models.CharField(max_length=200,  verbose_name='广告描述')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title


