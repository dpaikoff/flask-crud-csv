import pandas as pd
from io import StringIO
from flask import request, make_response, render_template, redirect

from app import app, db


@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        df = pd.read_csv(f.stream)
        df.to_sql('items', con=db.engine, if_exists='replace', index=False)
        # return render_template('admin/upload_success.html')
        return redirect('admin/upload_success')


@app.route('/download_file', methods = ['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        df = pd.read_sql('items', con=db.engine)
        buffer = StringIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        response = make_response(buffer.getvalue())
        cd = 'attachment; filename=items.csv'
        response.headers['Content-Disposition'] = cd
        response.mimetype='text/csv'
        return response

