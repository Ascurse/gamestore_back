from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название жанра'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='url-адрес жанра',
    )
    color = models.CharField(
        max_length=20,
        verbose_name='Цвет категории',
        default='#red'
    )

    class Meta:
        ordering = ('slug', )
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Game Title'
    )
    description = models.TextField(
        verbose_name='Game Description',
        blank=True
    )
    year = models.PositiveIntegerField(
        verbose_name='Creation Year',
        default=0,
        db_index=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='games',
        blank=True,
        verbose_name='Genres'
    )
    image = models.ImageField(
        verbose_name='Game Image',
        upload_to='games/',
        blank=True
    )
    video = models.CharField(
        verbose_name='Game Video',
        max_length=500,
        blank=True
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name='Game Price',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-year', ]


class News(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='News Title',
        blank=False,
    )
    post = models.TextField(
        verbose_name='Post Description',
        blank=False
    )
    post_image = models.ImageField(
        verbose_name='Post Image',
        upload_to='posts/',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    related_game = models.ForeignKey(
        Game,
        verbose_name='Related game',
        related_name='games',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', ]
