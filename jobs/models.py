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
    company_name = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
    )


class Question(models.Model):
    question_type = models.CharField(
        max_length=200,
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
