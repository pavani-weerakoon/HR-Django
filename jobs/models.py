from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(
        max_length=200,
    )
    location = models.CharField(
        max_length=200,
    )
    company_email = models.EmailField(
        max_length=200,
        blank=True, null=True
    )
    owner = models.OneToOneField(
        "jobs.User", related_name='managing_company',
        on_delete=models.CASCADE,
        max_length=200,
        blank=True, null=True
    )


class User(AbstractUser):
    class Meta:
        abstract = True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        max_length=200,
    )
    last_name = models.CharField(
        max_length=200,
    )
    email = models.EmailField(
        max_length=200,
        blank=True, null=True
    )
    contact_number = models.IntegerField(
        null=True
    )
    company = models.ForeignKey(
        Company, related_name='company_user',
        on_delete=models.CASCADE,
    )


class Job(models.Model):
    role = models.CharField(
        max_length=200,
    )
    salary = models.IntegerField(
        null=True
    )
    company = models.ForeignKey(
        Company,  related_name='jobs',
        on_delete=models.CASCADE,
    )


class Section(models.Model):
    section_name = models.CharField(
        max_length=200,
    )


class Question(models.Model):
    question_type = models.CharField(
        max_length=200,
    )
    section = models.ForeignKey(
        Section,  related_name='questions',
        on_delete=models.CASCADE,
    )
    job = models.ManyToManyField(
        Job, related_name='questions',

    )


class Candidate(User):
    cv = models.FilePathField(
        null=True, blank=True
    )
    job = models.ManyToManyField(
        Job, related_name='candidates'

    )


class Interviewer(User):
    role = models.CharField(
        max_length=200,
    )


class Interview(models.Model):
    interviewer = models.ForeignKey(
        Interviewer, related_name='interviews',
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        Interviewer, related_name='candidates',
        on_delete=models.CASCADE,
    )


class Experience(models.Model):
    role = models.CharField(
        max_length=200,
    )
    worked_place = models.CharField(
        max_length=100,
    )
    time_period = models.CharField(
        max_length=200,
    )
    Candidate = models.ForeignKey(
        Candidate, related_name='experiences',
        on_delete=models.CASCADE,
    )


class Admin(User):
    admin_role = models.CharField(
        max_length=200,
    )
