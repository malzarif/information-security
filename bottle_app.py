import os
from bottle import default_app, route, run, redirect, request, response

@route('/')
def get_index():
    redirect('/public')

@route('/public')
def get_public():
    return 'This public message should be shown to everyone!'

@route('/secret')
def get_secret():
    if request.get_cookie("user","false")=="true":
        return 'This secret message should only be shown to authorized people!'
    else:
        return 'Nothing'

@route('/login')
def get_login():
    response.set_cookie("user","true")
    return("ok, it looks like you logged in")

@route('/logout')
def get_logout():
    response.set_cookie("user","false")
    return("ok, it looks like you logged out")

if "PYTHONANYWHERE_DOMAIN" in os.environ:
    application = default_app()
else:
    run(host='localhost', port=8081)
