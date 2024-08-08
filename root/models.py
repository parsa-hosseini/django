from django.db import models

class sevices(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No descriptions.')
    status = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name


class sservices(models.Model):
    name = models.CharField(max_length=100)
    descrip = models.TextField(default='No descriptions.')
    status = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name  


class askes(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class trainer(models.Model):
    name = models.CharField(max_length=100)
    skil = models.CharField(max_length=100)
    bio = models.TextField(default='')
    prof = models.ImageField(upload_to='trainer' , default='Default_trainer.png')
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class vijegit(models.Model):
    text = models.TextField(default = '')    

    def __str__(self):
        return self.text

class vijegif(models.Model):
    text = models.TextField(default = '')    

    def __str__(self):
        return self.text

class price(models.Model):
    name = models.CharField(max_length=100)
    descrip = models.TextField(default='No descriptions.')
    price = models.IntegerField()
    time = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    vt = models.ManyToManyField(vijegit)
    vf = models.ManyToManyField(vijegif)

    def __str__(self):
        return self.name
