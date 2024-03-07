from django.db import models
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from globals.background import run
from threading import Thread
TYPE = (
    ('img','img'),
    ('video','video'),
)

class Watermark (models.Model) :
    type = models.CharField(choices=TYPE,max_length=100)
    original = models.FileField(upload_to='original-data/')
    output_path = models.CharField(max_length=1000)
    user = models.ForeignKey('users.User',related_name='user_watermark',on_delete=models.SET_NULL,null=True)
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4,db_index=True)
    text = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.text
    
@receiver(post_save,sender=Watermark)
def RunProcess (created,instance, **kwargs) : 
    if created:
        t = Thread(target=run,args=(instance,))
        t.start()