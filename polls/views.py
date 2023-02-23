from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect
from .models import Question, Choice


def index(request):
    """
    It takes a request, renders the index.html template, and returns the result

    :param request: This is the request object that is sent to the view
    :return: The render function is being called. The render function takes three arguments: the request, the template, and
    a dictionary. The request is the request object that is passed to the view. The template is the template that is being
    rendered. The dictionary is a dictionary of values that are passed to the template.
    """
    return render(request, 'index.html', {})
    #return HttpResponse('Hello world. Your at the polls index.')






def detail(request, poll_id):
    """
    It takes a request and a poll_id, fetches the Question object with that id, and passes it to a template

    :param request: The current HTTP Request object
    :param poll_id: The primary key of the poll we're interested in
    :return: The poll object is being returned.
    """
    poll = get_object_or_404(Question, pk=poll_id)
    return render(request, 'detail.html', {'poll': poll})


def results(request, poll_id):
    """
    If the request is a POST, then we process the data and redirect to the results page. If the request is not a POST, then
    we display the results page

    :param request: The current HTTP Request object
    :param poll_id: The primary key of the poll we're interested in
    :return: The results of the poll.
    """
    poll = get_object_or_404(Question, pk=poll_id)
    if request.method == 'POST':
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', poll_id=poll.id)
    else:
        return render(request, 'results.html', {'poll': poll})



def vote(request, poll_id):
    """
    It gets the Choice object with the given ID, increments its votes by one, and then calls save() to update the database

    :param request: The full HTTP request object
    :param poll_id: The primary key of the poll we're voting on
    :return: The poll object is being returned.
    """
    poll = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', poll_id=poll.id)


def poll(request):
    """
    If the request is a POST request, then get the poll object from the database and redirect to the detail page for that
    poll. Otherwise, just render the poll page with all the polls

    :param request: The full HTTP request object
    :return: The poll.html template is being returned.
    """
    questions = Question.objects.all()
    selected_poll = None
    if request.method == 'POST':
        selected_poll = get_object_or_404(Question, id=request.POST.get('poll_id'))
        return redirect('polls:detail', poll_id=selected_poll.id)
    return render(request, 'poll.html', {'questions': questions, 'selected_poll': selected_poll})
