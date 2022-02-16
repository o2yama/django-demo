# Django demo

## プロジェクト生成
 django-admin startproject　project-name

## 生成ファイル
#### __init__.py
 中身は空、このプロジェクトがPythonのパッケージであることを表す
#### setting.py 
 Djangoに関する設定を記述する
#### manage.py
 django-adminコマンドを使うときのスクリプト
 このスクリプトで開発サーバーやテストを行う
#### urls.py
 ルーティング関連
#### asgi.py, wsgi.py
 特に触ることはない

##　言語設定、タイムゾーン
setting.py >    LANGAGE_CODE = 'ja'     デフォルト: 'en-us'
                TIME_ZONE='Asia/Tokyo'  デフォルト: 'UTC'

## DB セットアップ
 setting.py >    BASE_DIR, DATABASES
##### python manage.py migrate
 テーブル作成
 Djangoでは元々、セッション管理やユーザー管理といった機能を提供するための、モデル定義とマイグレーションファイルが存在する。このコマンドでDBに反映される

## アプリケーション作成
 setting.py >　INSTALLED_APPS にアプリケーションの一覧を記述する

##### デフォルト
 INSTALLED_APPS = [
    'django.contrib.admin',         管理画面の機能
    'django.contrib.auth',          認証機能
    'django.contrib.contenttypes',  Content-Typeに関する機能
    'django.contrib.sessions',      セッション管理機能
    'django.contrib.messages',      フラッシュメッセージのためのアプリ
    'django.contrib.staticfiles',   静的ファイルに関する機能
 ]

##　スニペット管理のためのアプリ作成
 python manage.py startapp app-name
##### adimin.py 
 管理画面の設定を記述
##### apps.py
アプリの状態にフックする処理を記述
##### model.py
 DBのスキーマ定義
##### test.py
 テストを記述
##### view.py
 ビューを記述

'snippets.apps.SnippetsConfig' -> INSTALLED_APPSに追記

## テストコマンド
 python manage.py test
 test.py　の中身を実行

## サーバー立ち上げ
 python manage.py runserver

## DB
#### モデル定義
 1.<app/dir>/models.py にモデルを定義
 2.manage.py makemigrationsコマンドで、マイグレーションファイル作成
 3.manage.py migrateコマンドで、マイグレーションファイルからSQLを発行しテーブル作成

## 管理画面
 admin.py で admin.site.register(ModelName) -> models.pyで定義したモデル名のテーブル作成
 
#### 管理画面用ログインユーザ作成
 python manage.py createsuperuser -> ユーザ名、メール、パスワード入力(メールは適当でOK)
 