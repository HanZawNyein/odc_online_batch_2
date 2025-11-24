from odoo import api, fields, models


class IcaDepartment(models.Model):
    _name = 'ica.department' # ica_university
    _description = 'Ica Department'

    name = fields.Char(required=True)
    university_id = fields.Many2one('ica.university', required=True)
    parent_department_id = fields.Many2one('ica.department')