from django.db import models
from sklearn.cluster import KMeans
import joblib


# Create your models here.
class Customer(models.Model):
    Annual_Income= models.PositiveIntegerField(null=True)
    Spending_score=models.PositiveIntegerField(null=True)
    prediction=models.CharField(blank=True,null=True,max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        ml_model =joblib.load("ml_model/Segment.joblib")
        self.prediction= ml_model.predict([[self.Annual_Income, self.Spending_score]])
        return super().save(*args,**kwargs)

    class Meta:
        ordering=['-date']


    def _int_(self):
        return self.Annual_Income,self.Spending_score
        
