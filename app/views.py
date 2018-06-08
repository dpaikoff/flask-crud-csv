from flask_admin.contrib.sqla import ModelView

from app import db, admin
from .models import Items

admin.add_view(ModelView(Items, db.session))

