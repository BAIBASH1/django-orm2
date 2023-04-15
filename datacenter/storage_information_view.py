from datacenter.models import Visit
from django.shortcuts import render
import django
from datacenter.passcard_info_view import is_strange


def get_duration(visit):
    duration = django.utils.timezone.localtime() - visit
    return duration


def format_duration(duration):
    str_duration = str(duration).split('.')[0]
    return str_duration


def storage_information_view(request):
    non_closed_visits = []
    for visiter in Visit.objects.filter(leaved_at=None):
        element = {
            'who_entered': visiter.passcard.owner_name,
            'entered_at': visiter.entered_at,
            'duration': format_duration(get_duration(visiter.entered_at)),
            'is_strange': is_strange(visiter)
        }
        non_closed_visits.append(element)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
