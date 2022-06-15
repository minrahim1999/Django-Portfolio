from django.db import models

# Create your models here.


class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    fullName = models.CharField("My Full Name", max_length=100)
    position = models.CharField("My Position", max_length=100)
    introduction = models.TextField()
    profileImage = models.ImageField(
        "My Profile Image", upload_to=None, height_field=None, width_field=None, max_length=None)
    resume = models.FileField("My Resume", upload_to=None, max_length=100)
    description = models.TextField()
    projectsCompleted = models.IntegerField()
    yearsExperience = models.IntegerField()
    clientReviews = models.IntegerField()
    customerReviews = models.IntegerField()
    address = models.CharField("My Address", max_length=200)
    email = models.EmailField("My Email", max_length=254)
    education = models.CharField("Graduated from", max_length=100)
    phoneNumber = models.CharField("My Phone Number", max_length=50)
    facebookLink = models.CharField("Facebook Link", max_length=150)
    linkedInLink = models.CharField("LinkedIn Link", max_length=150)
    githubLink = models.CharField("GitHub Link", max_length=150)
    instagramLink = models.CharField("Instagram Link", max_length=150)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.fullName

    # TODO: Define custom methods here


class Skill(models.Model):
    """Model definition for Skill."""

    # TODO: Define fields here
    skillName = models.CharField("Skill Name", max_length=100)
    skillScore = models.CharField("Skill Score", max_length=50)

    class Meta:
        """Meta definition for Skill."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        return self.skillName

    # TODO: Define custom methods here


class Certificate(models.Model):
    """Model definition for Certificate."""

    # TODO: Define fields here
    certificateName = models.CharField("Certificate Name", max_length=100)
    certificateBadge = models.ImageField(
        "Certificate Badge", upload_to=None, height_field=None, width_field=None, max_length=None)
    certificateFile = models.FileField(
        "Certificate File", upload_to=None, max_length=100)

    class Meta:
        """Meta definition for Certificate."""

        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        """Unicode representation of Certificate."""
        return self.certificateName

    # TODO: Define custom methods here


class WorkExperience(models.Model):
    """Model definition for WorkExperience."""

    # TODO: Define fields here
    dateFrom = models.DateField(
        "Date From", auto_now=False, auto_now_add=False)
    dateUntil = models.DateField(
        "Date Until", auto_now=False, auto_now_add=False)
    workPosition = models.CharField("Work Position", max_length=100)
    experienceLevel = models.CharField("Experience Level", max_length=100)
    jobDescription = models.TextField()

    class Meta:
        """Meta definition for WorkExperience."""

        verbose_name = 'WorkExperience'
        verbose_name_plural = 'WorkExperiences'

    def __str__(self):
        """Unicode representation of WorkExperience."""
        return self.workPosition

    # TODO: Define custom methods here


class Project(models.Model):
    """Model definition for Project."""

    # TODO: Define fields here
    projectName = models.CharField("Project Name", max_length=100)
    projectLink = models.CharField("Project GitHub Link", max_length=50)
    projectImage = models.ImageField(
        "Card Image", upload_to=None, height_field=None, width_field=None, max_length=None)
    liveLink = models.CharField("Live Link", max_length=50)

    class Meta:
        """Meta definition for Project."""

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        """Unicode representation of Project."""
        return self.projectName

    # TODO: Define custom methods here


class Language(models.Model):
    """Model definition for Language."""

    # TODO: Define fields here
    language = models.CharField("My Language", max_length=50)

    class Meta:
        """Meta definition for Language."""

        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        """Unicode representation of Language."""
        return self.language

    # TODO: Define custom methods here
