from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView

from app import db, admin
from .models import Items


class UploadView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/upload.html', admin=admin)


class UploadSuccessView(BaseView):
    def is_visible(self):
        return False

    @expose('/')
    def index(self):
        return self.render('admin/upload_success.html', admin=admin)


class DownloadView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/download.html', admin=admin)


admin.add_view(ModelView(Items, db.session))
admin.add_view(UploadView('Upload', url='upload'))
admin.add_view(UploadSuccessView('UploadSuccess', url='upload_success'))
admin.add_view(DownloadView('Download', url='download'))

