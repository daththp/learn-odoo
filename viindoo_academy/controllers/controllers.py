from odoo import http

class ViindooAcademy(http.Controller):
    @http.route('/viindoo_academy', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('viindoo_academy.index', {
            'teachers':Teachers.search([])
        })

    @http.route('/viindoo_academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('viindoo_academy.biography', {
            'person': teacher
        })
