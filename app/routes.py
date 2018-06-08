import json
import pandas as pd
from io import StringIO
from flask import request, make_response, redirect

from app import app, db


@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            df = pd.read_csv(f.stream)
            df.to_sql('items', con=db.engine, if_exists='replace', index=False)
            return redirect('admin/upload_success')
        except Exception as e:
            content = {'error': str(e), 'status': 500}
            return json.dumps(content)


@app.route('/download_file', methods = ['GET', 'POST'])
def download_file():
    if request.method == 'GET':
        try:
            df = pd.read_sql('items', con=db.engine)
            buffer = StringIO()
            df.to_csv(buffer, index=False)
            buffer.seek(0)
            response = make_response(buffer.getvalue())
            cd = 'attachment; filename=items.csv'
            response.headers['Content-Disposition'] = cd
            response.mimetype='text/csv'
            return response
        except Exception as e:
            content = {'error': str(e), 'status': 500}
            return json.dumps(content)

