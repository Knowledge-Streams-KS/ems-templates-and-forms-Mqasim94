from django.shortcuts import render
from .models import Event, Registration
from .forms import EventForm, RegistrationForm

def eventlist(request):

    events = Event.objects.all()
    return render(request, 'app/eventlist.html', {"events":events} )

def eventdetail(request, event_id):

    event = Event.objects.get(id=event_id)
    return render(request, 'app/eventdetail.html', {'event':event})
    

def registerforevent(request, event_id):

    event = Event.objects.get(id=event_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = Registration(
                event=event,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )

            registration.save()
            return render(request, 'app/registerconfirmation.html')
    else:
        form = RegistrationForm()

    return render(request, 'app/register.html', {'event': event, 'form': form})
