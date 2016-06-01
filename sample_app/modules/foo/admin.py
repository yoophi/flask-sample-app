from os import path

from flask import current_app
from flask.ext.admin.contrib import sqla
from flask_admin_s3_upload import S3ImageUploadField
from speaklater import make_lazy_string

from sample_app import create_app_min
from .models import Thingy
from ...database import db
from ...extensions import admin
from ...library.admin_utils import ProtectedModelView
from ...library.prefix_file_utcnow import prefix_file_utcnow


def get_setting_value(key, default=None):
    try:
        return current_app.config.get(key, default)
    except RuntimeError as e:
        # logger.warning('current_app is inaccessible: %s' % e)
        pass

    try:
        app = create_app_min()
        db.init_app(app)
        with app.app_context():
            return app.config.get(key, default)
    except:
        return default

# def get_setting_value(key):
#     def get_config(key):
#         from flask import current_app as app
#
#         return app.config.get(key, '')
#
#     return make_lazy_string(lambda: get_config(key))


class ThingyView(sqla.ModelView):
    column_list = ('image',)
    form_excluded_columns = ('image_storage_type',
                             'image_storage_bucket_name')

    form_overrides = dict(
        image=S3ImageUploadField)

    form_args = dict(
        image=dict(
            base_path=get_setting_value('UPLOADS_FOLDER'),
            relative_path=get_setting_value('THINGY_IMAGE_RELATIVE_PATH'),
            url_relative_path=get_setting_value('UPLOADS_RELATIVE_PATH'),
            namegen=prefix_file_utcnow,
            storage_type_field='image_storage_type',
            bucket_name_field='image_storage_bucket_name',
        ))

    def scaffold_form(self):
        form_class = super(ThingyView, self).scaffold_form()
        static_root_parent = path.abspath(
            path.join(get_setting_value('PROJECT_ROOT'), '..'))

        if get_setting_value('USE_S3'):
            form_class.image.kwargs['storage_type'] = 's3'

        form_class.image.kwargs['bucket_name'] = get_setting_value('S3_BUCKET_NAME')
        form_class.image.kwargs['access_key_id'] = get_setting_value('AWS_ACCESS_KEY_ID')
        form_class.image.kwargs['access_key_secret'] = get_setting_value('AWS_SECRET_ACCESS_KEY')
        form_class.image.kwargs['static_root_parent'] = static_root_parent

        for k, v in form_class.image.kwargs.iteritems():
            print k, v

        print '=' * 80

        for k, v in self.form_args['image'].iteritems():
            print k, v

        return form_class

print '>' * 80
admin.add_view(ThingyView(Thingy, db.session, name='Thingies'))
print '<' * 80
