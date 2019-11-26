from django.db import models
import os
import random
import string

def randomStringGenerator():
    name = "I"
    name = name + str(random.randint(100, 999))
    letters = string.ascii_uppercase
    name = name + ''.join(random.choice(letters) for i in range(2))
    name = name + str(random.randint(10, 99))
    name = name + ''.join(random.choice(letters) for i in range(2))
    name = name + str(random.randint(100, 999))
    name = name + "."
    return name

    
def upload_location(instance, filename):
    extension = filename.split(".")[1]
    changed_file_name = randomStringGenerator()
    return "%s/%s%s" % ("item",changed_file_name, extension)
    

class File(models.Model):
    image = models.ImageField(null=True, upload_to=upload_location, blank=True)
