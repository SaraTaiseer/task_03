from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[{"restaurant_name":"Jubran","food_type":"Arabic food"},
    {"restaurant_name":"Mado","food_type":"Turkish food"},
    {"restaurant_name":"Chapatti","food_type":"Indian food"}
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{
    "restaurant_name ":"Leezet istanbul","food_type":"Turkish food"
    }

    }
    return render(request, 'detail.html', context)
