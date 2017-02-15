from datetime import datetime

from django.shortcuts import render
from action.forms import ActionCreateForm
from django.views.generic.list import ListView
from django.views.generic import View, UpdateView, CreateView, DeleteView
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from action.models import ActionManagement


# Create your views here.
class ActionList(ListView):
    """
    List the all Action
    """
    model = ActionManagement
    template_name = 'action/action_list.html'

    def get_queryset(self):
        return ActionManagement.objects.all()

    def get(self, request):
        try:
            start_date = datetime.strptime(self.request.GET['start_date'], "%Y-%m-%d")
            end_date = datetime.strptime(self.request.GET['end_date'], "%Y-%m-%d")
        except:
            object_list = ActionManagement.objects.all() # Get initial all queryset object
        else:
            object_list = ActionManagement.objects.filter(date__gte=start_date, date__lte=end_date)
        return render(request, self.template_name, {'object_list':object_list})



class ActionCreateView(View):
    """
    Create Action without use of CreateView class to show one type of create object
    """
    template_name = 'action/action_create.html'

    def get(self, request):
        form = ActionCreateForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ActionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list')
        else:
            return render(request, self.template_name, {'form':form})
        


class ActionEditView(UpdateView):
    """
    Edit object using Pure class base view
    """

    model = ActionManagement
    template_name = 'action/action_edit.html'
    form_class = ActionCreateForm
    success_url = reverse_lazy('action_list')


class ActionDeleteView(DeleteView):
    """
    Delete the Action object
    """
    model = ActionManagement
    template_name = 'action/action_confirm_delete.html'
    success_url = reverse_lazy('action_list')
