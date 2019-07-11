from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogApp1/post_list.html', {
            'posts' : posts,
            })  #ひとつ目の引数はerquest、2つ目は表示するhtmlファイル、3つ目はhtmlを表示するときに使うデータベースの情報
