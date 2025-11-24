from odoo import api, fields, models


class IcaUniversity(models.Model):
    _name = 'ica.university' # ica_university
    _description = 'IcaUniversity'

    name = fields.Char(required=True)
    founding_date = fields.Date()
    department_ids = fields.One2many('ica.department', 'university_id')
    logo = fields.Image()