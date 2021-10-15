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

    )


class User(AbstractUser):
    CANDIDATE = 'CA',
    INTERVIEWER = 'IN',
    ADMIN = 'AD',
    TYPES_OF_USERS = [
        (CANDIDATE, 'Candidate'),
        (INTERVIEWER, 'Interviewer'),
        (ADMIN, 'Admin'),
    ]
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
    choices = TYPES_OF_USERS


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
    job = models.ForeignKey(
        Job, related_name='questions',
        on_delete=models.CASCADE,
    )


class Candidate(models.Model):
    cv = models.FilePathField(
        null=True, blank=True
    )
    jobs = models.ManyToManyField(
        Job, related_name='candidates'

    )
    user = models.OneToOneField(
        User, related_name='candidates',
        on_delete=models.CASCADE,
        max_length=200,

    )


class Interviewer(models.Model):
    role = models.CharField(
        max_length=200,
    )
    user = models.OneToOneField(
        User, related_name='Interviewers',
        on_delete=models.CASCADE,
        max_length=200,

    )


class Interview(models.Model):
    interviewer = models.ForeignKey(
        Interviewer, related_name='interviews',
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        Interviewer, related_name='interviews',
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


class Admin(models.Model):
    admin_role = models.CharField(
        max_length=200,
    )
    user = models.OneToOneField(
        User, related_name='company_admin',
        on_delete=models.CASCADE,
        max_length=200,

    )
