from odoo import api, fields, models


class IcaUniversity(models.Model):
    _name = 'ica.university' # ica_university
    _description = 'IcaUniversity'

    name = fields.Char(required=True)


