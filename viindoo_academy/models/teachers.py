import datetime
from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'
    _description = 'Teachers'
    
    name = fields.Char(
        string='Name',
        help="The name of teacher",
        required=True)
    biography = fields.Html()
    birth_date = fields.Date(required=True)
    age = fields.Integer(compute='_compute_age',store=True)
    @api.depends('birth_date')
    def _compute_age(self):
        this_year = datetime.datetime.now()
        for r in self:
            if r.birth_date:
                r.age = int(this_year.strftime("%Y"))-int(r.birth_date.strftime("%Y"))
            else:
                r.age = 0
