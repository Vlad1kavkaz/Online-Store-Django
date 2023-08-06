from django.db import models
from django.urls import reverse


class Product(models.Model):
    BLUDANAMANGALE = "BM"
    HLEB = "HL"
    TORTIIPIROZHNIE = "TP"
    PIROGIMYASNIE = "PM"
    PIROGIOVOSHNIE = "PO"
    ZAPEKANIEMYASA = "ZM"
    ZAPEKANIEPTITSI = "ZP"
    ZAPEKANIERIBI = "ZR"
    ZHARKOE = "ZH"
    SALATI = "SA"
    ROGALIKI = "RO"
    MAK = "MA"
    BLINI = "BL"
    PELMENI = "PE"
    MILK = "MI"
    HONEY = "HO"
    HOTDRINKS = "HD"

    CATEGORY_CHOISE = [
        (BLUDANAMANGALE, 'Блюда на мангале'),
        (HLEB, 'Хлеб'),
        (TORTIIPIROZHNIE, 'Торты и пирожные'),
        (PIROGIMYASNIE, 'Пироги мясные'),
        (PIROGIOVOSHNIE, 'Пироги с овощной начинкой'),
        (ZAPEKANIEMYASA, 'Запекание мяса'),
        (ZAPEKANIEPTITSI, 'Запекание птицы'),
        (ZAPEKANIERIBI, 'Запекание рыбы'),
        (ZHARKOE, 'Жаркое с овощами'),
        (SALATI, 'Салаты'),
        (ROGALIKI, 'Рогалики, булки и печенье'),
        (MAK, 'Изделия с маковой начинкой'),
        (BLINI, 'Блины'),
        (PELMENI, 'Пельмени и вареники'),
        (MILK, 'Молоко, сметана, масло и творог'),
        (HONEY, 'Мёд'),
        (HOTDRINKS, 'Горячие напитки'),
    ]

    title = models.CharField('Название', max_length= 200)
    descriptoin = models.TextField('Описание', max_length= 500, default='--')
    compound = models.TextField('Состав', max_length= 500, default='--')
    image = models.ImageField('Фото', upload_to= 'img/')
    categoty = models.CharField('Категория', max_length= 100, choices=CATEGORY_CHOISE)
    cost = models.IntegerField('Цена', default=0, null=False)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return self.image.url

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])