from django.db import models
import random
from django.utils import timezone
import datetime


class User(models.Model):
    number = models.CharField(max_length=13)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.number

    def generate(self):
        self.number = str(random.randint(1000000000000, 9999999999999))
        self.name = f'Номер {random.randint(0, 9999999999999)}'
        super(User, self).save()
        for i in range(1, random.randint(2, 6)):
            Session().generate(self.name, i)

    def getChild(self):
        data = {
                'number':self.number,
                'name':self.name,
                'sessions':[],
             }
        for i in Session.objects.filter(parent__name=self.name):
            data['sessions'].append(
                {
                    'created_at':i.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    'session_id':i.session_id,
                    'actions':i.getChild()
                }
            )
        return data


class Session(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    session_id = models.CharField(max_length=100)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)

    def generate(self, ParentObject, j):
        self.session_id = self.generateSessionId()
        self.parent = User.objects.filter(name=ParentObject)[0]
        self.created_at = timezone.now() + datetime.timedelta(minutes=j)
        super(Session, self).save()
        for i in range(1, random.randint(3, 20)):
            Action().generate(self.session_id, i)

    def getChild(self):
        return [{'type':i.type, 'getChild':i.created_at.strftime("%m/%d/%Y, %H:%M:%S")} for i in Action.objects.filter(parent__session_id=self.session_id)]

    def generateSessionId(self):
        return ''.join([random.choice('q w e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9'.split()) for i in range(50)])


class Action(models.Model):
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_created=True)
    parent = models.ForeignKey(Session, on_delete=models.CASCADE)

    def generate(self, ParentObject, i):
        self.type = random.choice(['create', 'read', 'update', 'delete'])
        self.created_at = timezone.now() + datetime.timedelta(minutes=i)
        self.parent = Session.objects.filter(session_id=ParentObject)[0]
        super(Action, self).save()
