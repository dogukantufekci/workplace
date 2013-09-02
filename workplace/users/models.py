from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
)
from django.db import models

from workplace.constants import MaxLengths


class UserManager(BaseUserManager):
    def create_user(
        self,
        identifier,
        person,
        workplace,
        password=None
    ):

        if not identifier:
            msg = 'Each user must have an identifier'
            raise ValueError(msg)

        if not person:
            msg = 'Each user must have an person profile'
            raise ValueError(msg)

        if not workplace:
            msg = 'Each user must have an workplace'
            raise ValueError(msg)

        user = self.model(
            identifier=identifier,
            person=person,
            workplace=workplace,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        identifier,
        password,
    ):
        user = self.create_user(
            identifier=identifier,
            person=person,
            workplace=workplace,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    workplace = models.ForeignKey('workplaces.Workplace', related_name='users')
    person = models.OneToOneField('people.Person', related_name='person')

    identifier = models.CharField(db_index=True, max_length=MaxLengths.IDENTIFIER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['person', 'workplace',]
    
    def get_full_name(self):
        return self.person.get_full_name()
    
    def get_short_name(self):
        return self.identifier

    def __unicode__(self):
        return self.identifier

    class Meta:
        unique_together = (('workplace', ''),)