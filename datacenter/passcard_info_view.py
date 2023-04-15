from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import django
from django.shortcuts import get_object_or_404


SECONDS_IN_HOUR = 3600


def get_duration(visit):
    entered_time = visit.entered_at
    if visit.leaved_at:
        leaved_time = visit.leaved_at
    else:
        leaved_time = django.utils.timezone.localtime()

    duration = leaved_time - entered_time
    return duration


def format_duration(duration):
    str_duration = str(duration).split('.')[0]
    return str_duration


def is_strange(visit):
    if get_duration((visit)).total_seconds() > SECONDS_IN_HOUR:
        return True
    return False


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_strange(visit)
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
