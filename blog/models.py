from django.db import models

# Create Table called "Post"
class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField() # TextField ไม่จำกัดตัวอักษร
    
    # Dundle method
    def __str__(self):
        return self.title
# Migrations ->  Table to Database (Update DB)
# Migrate (บอกให้รู้ว่ามันมีการอัพเดท)
