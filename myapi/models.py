from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    treatments = models.TextField()
    symptoms = models.ManyToManyField("Symptom", related_name="diseases")

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


