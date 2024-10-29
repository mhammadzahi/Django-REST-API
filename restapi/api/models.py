from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key=True)# optional
    
    # Username field
    username = models.CharField(max_length=150, unique=True)
    
    # Email field
    email = models.EmailField(unique=True)
    
    # Password field
    password = models.CharField(max_length=128)  # Typically hashed passwords have a fixed length
    
    # Created_at field: requires manual entry of date/time
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.username
