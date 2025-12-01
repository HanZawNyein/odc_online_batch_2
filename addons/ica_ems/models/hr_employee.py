from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    class_ids = fields.One2many('ica.class','employee_id')
    class_count = fields.Integer(compute="_compute_class_count")

    @api.depends('class_ids')
    def _compute_class_count(self):
        for rec in self:
            rec.class_count = len(rec.class_ids)

