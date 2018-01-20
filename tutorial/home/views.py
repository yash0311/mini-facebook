from django.views.generic import TemplateView
from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from home.forms import HomeForm
from home.models import Post,Friend
from django.contrib.auth.models import User

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        form=HomeForm()
        posts=Post.objects.all().order_by('-created')
        users=User.objects.exclude(pk=request.user.pk)
        try:
            friend=Friend.objects.get(current_user=request.user)
        except Friend.DoesNotExist:
            friend=None
        if friend:
            friends = friend.users.all()
        else:
            friends = None

        args={'form':form,'posts':posts,'users':users,'friends':friends}
        return render(request,self.template_name,args)

    def post(self,request):
        form=HomeForm(request.POST)
        text=''
        if form.is_valid():
            post_object=form.save(commit=False)
            post_object.user = request.user
            form.save()
            text=form.cleaned_data['post']
            form=HomeForm()
            return HttpResponseRedirect(reverse('home:home'))

        args={'form':form,'text':text}
        return render(request,self.template_name,args)

def change_friend(request,operation,pk):
    new_friend=User.objects.get(pk=pk)
    #print(operation,pk)
    if operation == 'add':
        Friend.make_friend(request.user,new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user,new_friend)
    return redirect('home:home')


def message_to_friend(request):
    print(request)
    return redirect('home:home')
