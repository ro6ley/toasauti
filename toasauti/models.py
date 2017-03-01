from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


# Create your models here.
def upload_img_path(instance, filename):
    return 'toasauti/static/uploads/image/{0}'.format(filename)


def upload_vid_path(instance, filename):
    return 'toasauti/static/uploads/video/{0}'.format(filename)


def upload_aud_path(instance, filename):
    return 'toasauti/static/uploads/audio/{0}'.format(filename)


class Report(models.Model):
    OFFENCE_TYPE_CHOICES = (
        ('RD', 'Reckless Driving'),
        ('HR', 'Harassment'),
        ('BR', 'Bribery'),
        ('HNR', 'Hit and Run'),
        ('SP', 'Speeding'),
        ('AC', 'Accident'),
        ('OT', 'Other'),
    )

    VEHICLE_TYPE_CHOICES = (
        ('PR', 'Private Vehicle'),
        ('PB', 'Public Vehicle'),
        ('MC', 'Motor Cycle'),
    )

    carRegNo = models.CharField(max_length=50, verbose_name='Car Registration Number')
    vehicleType = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES, verbose_name='Vehicle Type')
    offenceType = models.CharField(max_length=20, choices=OFFENCE_TYPE_CHOICES, verbose_name='Offence Type')
    offenceDescription = models.TextField(max_length=400, verbose_name='Offence Description')
    location = models.CharField(max_length=200, verbose_name='Location')
    time = models.DateField(default=timezone.now, verbose_name='Date')
    image = models.ImageField(upload_to=upload_img_path, default=None, blank=True, null=True, verbose_name='Image(s)')
    video = models.FileField(upload_to=upload_vid_path, default=None, blank=True, null=True, verbose_name='Video(s)')
    audio = models.FileField(upload_to=upload_aud_path, default=None, blank=True, null=True, verbose_name='Audio(s)')
    userEmail = models.EmailField(max_length=20, default=None, verbose_name='Email')
    userPhoneNumber = models.CharField(max_length=20, default=None, verbose_name='Phone Number')
    userNames = models.CharField(max_length=200, default=None, verbose_name='Reported By')
    userIDNumber = models.CharField(max_length=20, default=None, verbose_name='ID Number')
    followedUp = models.BooleanField(max_length=10, default=0, verbose_name='Has it been followed up and logged')
    details = models.TextField(max_length=500, default=None, blank=True, null=True, verbose_name='Details')

    def __str__(self):
        return self.carRegNo+" at "+self.location

    def image_tag(self):
        if self.image:
            img = str(self.image)[8:]
            return mark_safe('<a href="{0}" target="_blank"> <img src="{0}" width="500" height="300"> </a>'.format(img))

        else:
            return mark_safe('No Image(s) available')

    image_tag.short_description = 'Image(s)'

    def video_tag(self):
        if self.video:
            vid = str(self.video)[8:]

            # For MP4 Videos
            if vid[-3:] == "mp4":
                return mark_safe('<video width="500" height="350" controls> <source src="{}" type="video/mp4"> <video/>'.format(vid))

            # For Ogg Videos
            elif vid[-3:] == "ogg":
                return mark_safe('<video width="500" height="350" controls> <source src="{}" type="video/ogg"> <video/>'.format(vid))

            # For WEBM Videos
            elif vid[-4:] == "webm":
                return mark_safe('<video width="500" height="350" controls> <source src="{}" type="video/webm"> <video/>'.format(vid))

        else:
            return mark_safe('No Video available')

    video_tag.short_description = 'Video'

    def audio_tag(self):
        if self.audio:
            aud = str(self.audio)[8:]

            # For MP3 Audio
            if aud[-3:] == "mp3":
                return mark_safe('<audio controls> <source src="{}" type="audio/mpeg"> </audio>'.format(aud))

            # For OGG Audio
            elif aud[-3:] == "ogg":
                return mark_safe('<audio controls> <source src="{}" type="audio/ogg"> </audio>'.format(aud))

            # For WAV Audio
            elif aud[-3:] == "wav":
                return mark_safe('<audio controls> <source src="{}" type="audio/wav"> </audio>'.format(aud))

        else:
            return mark_safe('No Audio available')

    audio_tag.short_description = 'Audio'


class Feedback(models.Model):
    firstName = models.CharField(max_length=20, verbose_name='First Name')
    lastName = models.CharField(max_length=20, verbose_name='Last Name')
    email = models.EmailField(max_length=50, verbose_name='Email Address')
    message = models.TextField(max_length=500, verbose_name='Message')

    def __str__(self):
        return self.firstName+" "+self.lastName+" "+self.email
