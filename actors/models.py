from django.db import models

class Actor(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    name = models.CharField(max_length=150)
    birth_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    profile_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'actors'
        ordering = ["name"]
        verbose_name = 'actor'
        verbose_name_plural = 'actors'

    def __str__(self):
        return self.name