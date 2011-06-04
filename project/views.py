from callsheet.models import Callsheet
from callsheet.forms import *
from project.models import Project
from project.forms import BasicProjectForm

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	projects = Project.objects.filter(owner=request.user)
	
	return render_to_response('project/index.html', {'projects':projects}, context_instance=RequestContext(request))
	
def new(request):
	if request.method == "POST":
		project_form = BasicProjectForm(request.POST)
		
		if project_form.is_valid():
			project = project_form.save(commit=False)
			project.owner = request.user
			project.save()
			return HttpResponseRedirect('/projects/' + str(project.pk) + '/')
	else:
		project_form = BasicProjectForm()
	
	return render_to_response('project/new.html', {"form": project_form,})
	

def detail(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	
	return render_to_response('project/detail.html', {'project': project}, context_instance=RequestContext(request))

def callsheets(request, project_id):
	callsheets = Callsheet.objects.filter(project=project_id)
	project = get_object_or_404(Project, pk=project_id)
	
	return render_to_response('project/callsheets.html', {'project': project, 'callsheets':callsheets}, context_instance=RequestContext(request))
	
