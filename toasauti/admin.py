from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = "Toa Sauti Administration"
admin.site.site_title = "Toa Sauti Administration"


def make_followed_up(modeladmin, request, queryset):
    queryset.update(followedUp=False)

make_followed_up.short_description = "Mark reports as followed up"


class ReportAdmin(admin.ModelAdmin):
    fields = ['carRegNo', 'vehicleType', 'offenceType', 'offenceDescription',
              'location', 'time',  # 'image', 'video', 'audio',
              'userEmail', 'userPhoneNumber', 'userNames', 'userIDNumber',
              'image_tag', 'video_tag', 'audio_tag', 'followedUp', 'details',
              ]
    list_display = ['carRegNo', 'offenceType', 'location', 'time', 'followedUp']
    ordering = ['time'].reverse()
    readonly_fields = ('carRegNo', 'vehicleType', 'offenceType', 'offenceDescription',
                       'location', 'time',  # 'image', 'video', 'audio',
                       'userEmail', 'userPhoneNumber', 'userNames', 'userIDNumber', 'image_tag', 'video_tag',
                       'audio_tag',
                       )
    actions = [make_followed_up]


class FeedbackAdmin(admin.ModelAdmin):
    fields = ['firstName', 'lastName', 'email', 'message']
    list_display = ['email', 'firstName', 'lastName', 'message']
    readonly_fields = ['firstName', 'lastName', 'email', 'message']


admin.site.register(Report, ReportAdmin)
admin.site.register(Feedback, FeedbackAdmin)
