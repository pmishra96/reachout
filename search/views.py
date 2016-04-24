from django.shortcuts import render
from reachout import settings

# Create your views here.
from django.http import HttpResponse
from backend.models import Client
from backend.models import Tag


def index(request):
    full_client_list = Client.objects.all()
    full_tags_list   = Tag.objects.all()
    client_list = []
    tags_list   = []
    template = "search.html"

    search_input = (request.POST.get('search_input'))
    if (search_input != None): search_input = search_input.lower()

    if (search_input == None or 
        search_input == ""   or 
        search_input == "enter tags"): 
        search_input = "enter tags"
        client_list = full_client_list

    print("SEARCH INPUT: ")
    print(search_input)

    for client in full_client_list: 
        if (client.first_name.lower() in search_input or
            client.last_name.lower() in search_input or
            client.nick_name.lower() in search_input or
            client.location.lower() in search_input):
            if (client not in client_list): 
                client_list.append(client)
        for word in client.visual_description.split(" "):
            word = ''.join(c for c in word if c.isalpha())
            word = word.lower()
            if word in search_input: 
                if (client not in client_list): 
                    client_list.append(client)
        for tag in client.get_tags(): 
            if (tag in search_input and client not in client_list):
                client_list.append(client) 





    context = {"client_list": client_list, 
               "search_input": search_input}
    return render(request, template, context)

