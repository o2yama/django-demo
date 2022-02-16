from django.contrib import admin
from django.urls import path, include
from snippets import views

urlpatterns = [
    path('', views.top, name='top'),
    path('snippets/', include('snippets.urls')), # snippets/urls.py の読み込み
    path('admin/', admin.site.urls),
]

# path
# 第一引数 : リクエストのパス、先頭の/は省略するため’’
# 第二引数 : ビュー関数、'/'にアクセスが来た時に呼び出す関数
# nameキーワード関数 : URLの逆引き時に使用

