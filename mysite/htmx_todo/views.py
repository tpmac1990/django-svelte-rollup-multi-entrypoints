from django.shortcuts import render
from .models import Todo


DELETE = "DELETE"
POST = "POST"
PUT = 'PUT'
    
def todo_tasks(request):

    if request.htmx:

        if request.method == DELETE:

            item_id = request.GET.get('id')

            Todo.objects.get(id=item_id).delete()

        elif request.method == POST:

            new_todo = request.POST.get('new-todo')
            Todo.objects.create(item=new_todo)

        elif request.method == PUT:

            item_id = request.GET.get('id')
            todo = Todo.objects.get(id=item_id)
            
            if 'checked' in request.GET:
                todo.complete = not todo.complete

            todo.save()

    context = {
        "todo_list": Todo.objects.filter(complete=False),
        "complete_list": Todo.objects.filter(complete=True),
    }
    
    if request.htmx:
        return render(request, 'htmx_todo/partials/todo_lists.html', context)
    return render(request, 'htmx_todo/index.html', context)


    




# is_htmx = self.request.headers.get('HX-Request') == 'true'

# from django.views.decorators.http import require_http_methods
# @require_http_methods(['DELETE'])
# def delete_task(request, id):

# from django.views.decorators.http import require_http_methods
