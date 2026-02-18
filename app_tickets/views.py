from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket

@login_required
def ticket_list(request):
    tickets = Ticket.objects.select_related('assigned_agent').order_by('-created_at')
    return render(request, 'app_tickets/ticket_list.html', {'tickets': tickets})
