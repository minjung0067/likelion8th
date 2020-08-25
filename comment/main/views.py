from django.views import generic
from .models import Post,Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    def get_queryset(self): #ListView에서 사용-표시 하려는 개체 목록을 결정한다. 
        return Post.objects.all()

class DetailView(generic.DetailView): #CBV , pk없이 인자 숫자로 템플릿 바로 데려오는? 
    model = Post #queryset = Post.objects.all()이랑 같은 기능<-FBV
    template_name = 'detail.html'   #렌더 어쩌고 대신 쓰는 것 
    context_object_name='ppost'  #어떤 이름으로 부를 건지 ! html에서 이 이름으로 접근

    def get_context_data(self, **kwargs):   #FBV에서는 어케 했냐면 ... { '' : } 안에 여러 개 써서 그럼 이 안에 애들이 context
        context_data = super(DetailView, self).get_context_data(**kwargs) #근데 CBV에서는 원칙적으로 하나 밖에 못 보내서 이 함수 써서 post 말고 comment같은 다른 것도 보내게
        context_data['form'] = CommentForm() #'' 속 이 이름을 통해서 템플릿에서 접근 {'얘':}랑 똑같음 
        context_data['comment'] = self.object.comment_set.all() #detail view에 있는 post의 옵젝트 , _set을 붙이면 포린키가 어디에 포린키로 엮여있는지 알고 싶을 때 모델이름_set.all하면 post가 갖고 있는 포린키들이 주루룩
        #글에 댓글 여러개인데 그걸 열람하고 싶어 하면 이거 써주면 됨 목록 쭈루룩 열람 ~~~! 팔로우하는 사람들 알고 싶을 때도 사용가능 '_set'
        #post 입장에서 나를 참조한 애들을 다 불러줘랑 같은 말~!~!!!!!!!!!!!!!!!!!!! self.object를 post로 대체할 수 없다 왜냐면 detail로 가져온 post 하나에 대한 거니까!
        return context_data #결과적으로는 context_data(ppost랑 form이랑 comment가 보내진 것 
        #super 부터는 필수 적으로 써야하는데 이건 기본 제공되는 getcontextdata 함수 오버라이딩!

def comment_create(request, post_id):
    if not request.user.is_anonymous: #익명이 아니냐 ! 로그인했냐! =is_authenticated(?)
        comment_form = CommentForm(request.POST) #request.post로 받아온 내용을 담겠다
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # commit은 잠시만 멈춰봐!!! form에서 content만 보내줬는데 content 말고 author랑 다른 거도 db에 보여줘야되니까
            comment.author = request.user #얘는 자동으로 받아오니까! request요청한 user를 담아줌
            comment.post_id = post_id
            comment.save()
        else: 
            messages.info(request, "올바르지 않은 댓글 형식입니다.")
    else: #로그인 안 하고 댓글 쓰면 메세지
        messages.info(request, "로그인이 필요합니다.")
    return HttpResponseRedirect(reverse('detail',args = (post_id,))) #render은 데이터 같이 보낼 때 , httpresponseredirect는 그런 거 없고 url만 연결할 때

def comment_update(request, comment_id,post_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.warning(request, "권한 없음")
        return HttpResponseRedirect(reverse('detail',args = (post_id,)))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail',args = (post_id,)))
    else:
        form = CommentForm(instance=comment)
    return render(request,'comment_update.html',{'form':form})


def comment_delete(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Post, pk=comment.post.id)

    if request.user != comment.author and not request.user.is_staff and request.user != post.author:
        messages.warning(request, '권한 없음')
        return redirect('home')

    if request.method == "POST":
        comment.delete()
        return redirect('home')
    else:
        return render(request, 'comment_delete.html', {'object':comment})

def dispatch(self, request, *args, **kwargs):
    object = self.get_object()
    if request.method == "POST":
        super().post(request, *args, **kwargs)
    else:   
        super().post(request, *args, **kwargs)