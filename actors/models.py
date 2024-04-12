from django.db import models


class Actor(models.Model):
    NATIONALITY_CHOICES = (
        ('AR', 'Argentinian'),
        ('BR', 'Brazilian'),
        ('CO', 'Colombian'),
        ('CL', 'Chilean'),
        ('EC', 'Ecuadorian'),
        ('MX', 'Mexican'),
        ('PE', 'Peruvian'),
        ('UY', 'Uruguayan'),
        ('VE', 'Venezuelan'),
        ('US', 'American'),
        ('CA', 'Canadian'),
        ('USR', 'Russian'),
    )

    name = models.CharField(max_length=200)
    birtday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
