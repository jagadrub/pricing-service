import flask
from flask_cors import CORS

from app.utils import config
from app.domain.price import route as pricing_routes
from app.domain.discount import route as discounts_routes
from app.gateways import rabbit_service

class MainApp:
    instance = None

    def __init__(self):
        # Init flask_app
        self.app = flask.Flask(__name__)
        CORS(self.app, support_credentials=True, automatic_options=True)

        # Init other apps
        self._init_pricing_routes()
        self._init_discounts_routes()
        self._init_rabbit()

        MainApp.instance = self.app

    def _init_pricing_routes(self):
        pricing_routes.init(self.app)

    def _init_discounts_routes(self):
        discounts_routes.init(self.app)

    def _init_rabbit(self):
        rabbit_service.init()

    def get_flask_app(self):
        return self.app

    def start(self, debug=True):
        self.app.run(port=config.get_server_port(), debug=debug)

    @staticmethod
    def wsgi(*args):
        if not MainApp.instance:
            MainApp()
        return MainApp.instance(*args)
