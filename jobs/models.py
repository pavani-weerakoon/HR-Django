from django.db import models

# Create your models here.


class Company(models.Model):
    company = models.CharField(
        max_length=200,
    )
    location = models.CharField(
        max_length=200,
    )
    company_email = models.EmailField(
        max_length=200,
        blank=True, null=True
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


class Candidate(models.Model):
    cv = models.FilePathField(
        null=True, blank=True
    )
    job = models.ManyToManyField(
        Job, related_name='candidates'

    )
    company = models.ForeignKey(
        Company,  related_name='candidates',
        on_delete=models.CASCADE,
    )


class User(models.Model):
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
        Company, related_name='users',
        on_delete=models.CASCADE,
    )


class Interviewer(models.Model):
    role = models.CharField(
        max_length=200,
    )
    company = models.ForeignKey(
        Company,  related_name='interviewers',
        on_delete=models.CASCADE,
    )


class Interview(models.Model):
    interviewer = models.ForeignKey(
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
