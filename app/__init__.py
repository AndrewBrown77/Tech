from flask import Flask
from app.routes import home
from app.routes import home, dashboard

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  @app.route('/hello')
  def hello():
    return 'Send It!'
  # register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  return app

  #should use a app key when creating on server side sessions 
   # python functions are set by two spaces not by semicolons or curley brackets
