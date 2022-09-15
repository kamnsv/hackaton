from flask import render_template, redirect, session, send_file, request
import os
import json
from pred import predict 


def start(app):

    app.config.from_object('config')
    app.secret_key = app.config['SECRET_KEY']     
    
    @app.route('/')
    def home():                   
        return render_template('index.html') 

    @app.route('/api', methods=('GET', 'POST'))
    def get_api():
        y = predict(request.get_json())
        if y is None: return abort(401)
        return json.dumps(y, indent=4, default=str, ensure_ascii=False)
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', title=404)
        
   