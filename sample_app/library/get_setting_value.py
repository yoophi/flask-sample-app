from flask import current_app

from sample_app import create_app_min, db


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
<<<<<<< e5f3039b74b02fa5d8f6b87dc78566d28bc7c142
        return default
=======
        return default

>>>>>>> s3 업로드 관련 모듈 샘플 추가
