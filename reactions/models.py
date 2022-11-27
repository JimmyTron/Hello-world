from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Here are my models
""" Abstract User """
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)
    phone_number = PhoneNumberField(blank=True, help_text='Contact phone number', null=True)
    verification_code = models.CharField(max_length=100, blank=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone_number'] # add phone number as a requirement while signing up

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

""" User Accounts """
class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#Referencing the customized user
    alias = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_picture = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.alias

""" Stori_category """
class Stori_category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"

""" Stori """
class Stori(models.model): #stori is swahili for story. was thinking of get the slang version 'risto'/'riba' in there..
    title = model.CharField(max_length=50)
    stori = model.CharField(max_length=280)#Using 280 here since its twitter's max characters for a single tweet 
    description = model.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    #category = "to figure the relationship type"

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Mastori"

""" Stori_comments """
class Stori_comment(models.Model):
    stori = models.ForeignKey(Stori, related_name='mastori', on_delete=models.CASCADE)
    reaction_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    
    def __str__(self):
        return self.comment

""" Reaction_choice """
class Reaction_choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    reaction_choice = models.CharField(max_length=50)

    def __str__(self):
        return self.reaction_choice

""" Stori_reactions """        
class Stori_reaction(models.Model):
    stori = models.ForeignKey(Stori,  on_delete=models.CASCADE)
    reaction_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction_choice, on_delete=models.CASCADE)# Do I realy have to keep this here?

    def __str__(self):
        return self.reaction

    class Meta:
        unique_together = ("comment", "reaction_by")

""" Comment Reactions """
class Comment_reaction(models.Model):
    comment = models.ForeignKey(Comment, related_name='comments', on_delete=models.CASCADE)
    reaction_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction_choice, on_delete=models.CASCADE)# Do I realy have to keep this here?

    def __str__(self):
        return self.reaction

    class Meta:
        unique_together = ("comment", "reaction_by")

