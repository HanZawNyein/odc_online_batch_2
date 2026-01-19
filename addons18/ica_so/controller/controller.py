from odoo import http
from odoo.http import request

class MainController(http.Controller):
    @http.route(['/app/rooms'],type='http',auth="public",website=True)
    def index(self):
        return request.render(
            "ica_so.main_template",
            {
                "data": "abc",
            },
        )