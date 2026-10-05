from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FacultyInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    coordinator_name = models.CharField(max_length=200)
    coordinator_contact = models.CharField(max_length=200)
    description = models.TextField()
    disciplines = models.TextField()
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="programs"
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="teachers"
    )

    def __str__(self):
        return self.name
