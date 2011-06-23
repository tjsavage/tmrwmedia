from project.groups.models import Group
from project.models import Project

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if not project.is_admin(request.user):
		return render_to_response('project/no_permission.html')
	
	GroupFormSet = modelformset_factory(Group, exclude=('project',), extra=2)
	if request.method == "POST":
		formset = GroupFormSet(request.POST, queryset=Group.objects.filter(project=project_id))
		if formset.is_valid():
			instances = formset.save(commit=False)
			for instance in instances:
				instance.project = project
				instance.save()
			return HttpResponseRedirect("/projects/" + str(project_id) + "/")
	else:
		formset = GroupFormSet(queryset=Group.objects.filter(project=project_id))
	
	
	return render_to_response("project/groups/edit.html", {
								"formset": formset,
								"project": project,
							},
							context_instance=RequestContext(request))

def index(request, project_id):
	return HttpResponse("Groups index.")