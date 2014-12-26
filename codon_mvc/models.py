from django.db import models

class CodonFrequency(models.Model):
    codon = models.CharField(max_length=3)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return self.codon

    def __str__(self):
        return self.frequency