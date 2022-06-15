from django.contrib import admin
from .models import (Profile,
                     Project,
                     Skill,
                     WorkExperience,
                     Certificate,
                     Language)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Certificate)
admin.site.register(Language)
