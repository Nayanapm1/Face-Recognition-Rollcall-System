from django.db import models

# Create your models here.

class Term(models.Model):
    TermId = models.AutoField(primary_key=True)
    TermName = models.CharField(max_length=45)

    class Meta:
        db_table='Term'