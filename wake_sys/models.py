from django.db import models
from django.contrib.auth.models import User
from PIL import Image

SLOTS = (
    (00, '00'),
    (15, '15'),
    (30, '30'),
    (45, '45'),
)

HOURS = (
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
    (19, '19'),

)

SLT = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    hour = models.IntegerField(choices=HOURS)
    start_slot = models.IntegerField(choices=SLOTS)
    duration = models.IntegerField(choices=SLT)
    instructor = models.BooleanField()
    gear = models.BooleanField()

    def __str__(self):
        return (f'Rezerwacja: {self.day}, godzina {self.hour}:{self.start_slot}, ilość miejść: {self.duration},'
                f' instuktor: {self.instructor}, sprzęt: {self.gear}')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
