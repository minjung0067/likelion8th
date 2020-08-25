# 댓글 작성 폼
from django import forms
from .models import Comment,Post

class CommentForm(forms.ModelForm): #장고문서에 있음

    class Meta: #commentform 을 상속받은 클래스? 규칙 같은 거?
        model = Comment #어떤 모델에 관련된 폼인지
        fields = ('content',) #사용자야 이것만 작성해조! 사용자한테 어떤 요소를 받을 건지
