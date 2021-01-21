from django.shortcuts import render
from django.views import View
from .models import User, Session, Action


class FirstTask(View):
    def get(self, request):
        return render(request, 'first/first_all_page.html', context={'UserData': User.objects.all()})

    def post(self, request):
        User().generate()
        return self.get(request)


class WatchJson(View):
    def get(self, request, num):
        return render(request, 'first/watchjson.html', context={'UserData': User.objects.all(),
                                                                'startdata': User.objects.filter(number=num)[0].getChild(),
                                                                'enddata': self.GenEndData(User.objects.filter(number=num)[0].getChild()),
                                                                })

    def GenEndData(self, jsonDat):
        dat = {
            'number': jsonDat['number'],
            'actions': [{
                'type': 'create',
            },
            {
                'type': 'read',
            },
            {
                'type': 'update',
            },
            {
                'type': 'delete',
            },]
        }
        all_dat = Action.objects.filter(parent__parent__number=jsonDat['number'])
        for id_, i in enumerate(['create', 'read', 'update', 'delete']):
            dat['actions'][id_]['count'] = all_dat.filter(type=i).count()
            if dat['actions'][id_]['count']:
                dat['actions'][id_]['last'] = all_dat.filter(type=i).order_by('created_at')[::-1][0].created_at.strftime("%m/%d/%Y, %H:%M:%S")
            else: dat['actions'][id_]['last'] = None
        return dat
