from email.mime import audio
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from snippets.forms import SnippetForm

from snippets.models import Snippet
from snippets.forms import SnippetForm

def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, 'snippets/top.html', context)


def snippets_list(request):
    return HttpResponse('all snippets list')


@login_required #このデコレータに囲まれたビューへのアクセスにはログインが必要
def snippet_new(request):
    if request.method == 'POST':
        # POSTメソッドだっった場合、入力データを取り出し、新規スニペットを作成
        form = SnippetForm(request.POST)
        if form.is_valid:
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        #GETメソッドだった場合、情報を入力するためのHTMLフォームを返す
        form = SnippetForm()
    return render(request, 'snippets/snippet_new.html', {'form': form})


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {"snippet": snippet})


@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)

    if snippet.created_by.id != request.user.id:
        return HttpResponseForbidden('このスニペットの編集は許可されていません')

    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid:
            form.save()
            return redirect(snippet_detail, snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})
