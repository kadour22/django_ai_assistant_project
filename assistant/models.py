import os
from openai import OpenAI

from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

api_key=os.getenv("XAI_API_KEY")
client = OpenAI(
  base_url=os.getenv("base_url"),
  api_key=api_key,
)

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True , related_name='issues')
    
    def __str__(self):
        return self.title
    

class products(models.Model):
        
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

@receiver(pre_save, sender=products)        
def generate_discription_with_ai(sender, instance, **kwargs):
        if not instance.description:
            response = client.chat.completions.create(
            model="x-ai/grok-4.1-fast:free",
            messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates product descriptions."},
                    {"role": "user", "content": f"Generate a detailed product small attractive description for a product named '{instance.name}'."}
                ])
                    
            instance.description = response.choices[0].message.content[:-1]
            instance.save()
            print("Description generated and saved.")
        print("Description already exists.")