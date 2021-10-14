from django.db import models

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


class Job(models.Model):
    role = models.CharField(
        max_length=200,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
    )


class section(models.Models):
    section_name = models.CharField(
        max_length=200,
    )


class Question(models.Model):
    question_type = models.CharField(
        max_length=200,
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
    )


class Candidate(models.Model):
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
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )
