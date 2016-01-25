#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'これは Index ページです'

@app.route('/hello')
def hello():
  return 'Hello World!! 日本語は？' + __name__

@app.route('/uer/<username>')
def show_user_profile(username):
  return u'ユーザー %s です' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  return 'Post %d ' % post_id

@app.route('/projects/')
def projects():
  return 'This is the project method.'

@app.route('/about')
def about():
  return 'This is the about page.'


if __name__ == '__main__':
  app.run(debug=True)

