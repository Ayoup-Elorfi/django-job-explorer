from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Job, Candidate
from django.core.paginator import Paginator
from .forms import CandidateForm, JobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from rest_framework import generics
from .serializers import JobSerializer


# class based view
class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


def job_list(request):
    jobs = Job.objects.all()
    myfilter = JobFilter(request.GET, queryset=jobs)
    jobs = myfilter.qs

    paginator = Paginator(jobs, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'myfilter': myfilter
    }
    return render(request, 'job/job_list.html', context)


@login_required
def view_candidates(request):
    candidate = Candidate.objects.all()
    context = {
        'candidate': candidate,
    }
    return render(request, 'candidate/candidates.html', context)


def job_detail(request, id):
    job_detail = Job.objects.get(id=id)

    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            new_candidate = form.save(commit=False)
            new_candidate.job = job_detail
            new_candidate.save()
    else:
        form = CandidateForm()

    context = {
        'job': job_detail,
        'form': form,
    }
    return render(request, 'job/job_detail.html', context)


@login_required
def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:jobs'))

    else:
        form = JobForm()

    return render(request, 'job/post_job.html', {'form': form})
