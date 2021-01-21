from django.shortcuts import render
from django.views import View
from .models import Accrual, Payment


class SecondTask(View):
    def get(self, request):
        return render(request, 'second/secondtask.html', context={'data': self.formirateData()})

    def formirateData(self):
        dat = {'sootv': [], 'not_Pay': [], 'not_Acc': []}
        use_dat = []
        all_payment = Payment.objects.all()  # платежи
        all_accrual = Accrual.objects.all()  # долги
        for i in all_accrual:
            for j in all_payment.filter(month=i.month):
                if i not in use_dat and j not in use_dat:
                    dat['sootv'].append(f'{i.id} - {i.date} - {i.month} | {j.id} - {j.date} - {j.month}')
                    use_dat.append(i)
                    use_dat.append(j)
        for i in all_accrual:
            if i not in use_dat:
                dat['not_Acc'].append(f'{i.id} - {i.date} - {i.month}')
        for i in all_payment:
            if i not in use_dat:
                dat['not_Pay'].append(f'{i.id} - {i.date} - {i.month}')
        return dat
