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
    company = models.ForeignKey(
        Company,
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
        Section,
        on_delete=models.CASCADE,
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
    )


class Candidate(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )


class User(models.Models):
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
        Company,
        on_delete=models.CASCADE,
    )


class Interviewer(models.Model):
    role = models.CharField(
        max_length=200,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )


class Interview(models.Models):
    interviewer = models.ForeignKey(
        Interviewer,
        on_delete=models.CASCADE,
    )


class Experience(models.Models):
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
        Candidate,
        on_delete=models.CASCADE,
    )


class Admin(models.Model):
    admin_role = models.CharField(
        max_length=200,
    )
