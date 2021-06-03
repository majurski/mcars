from cars.models import Car
from .forms import FilterForm
from django.views.generic.list import ListView
from django.db.models import Q

class Search(ListView):
    model = Car
    template_name = 'home.html'

    def get_queryset(self):
        query_1 = self.request.GET.get('filter_field_1')
        query_2 = self.request.GET.get('search')
        
        if query_1:
            return Car.objects.filter(
                Q(brand__icontains=query_1)
            )
        elif query_2:
            return Car.objects.filter(
                Q(brand__icontains=query_2)
            )
        else:
            return Car.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = FilterForm(initial={
            'search': self.request.GET.get('search', ''),
            'filter_field_1': self.request.GET.get('filter_field_1', ''),
        })

        return context