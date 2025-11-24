from odoo import api, fields, models


class IcaClass(models.Model):
    _name = 'ica.class'
    _description = 'IcaClass'

    name = fields.Char(required=True)
    company_id = fields.Many2one('res.country', string="University Name")
    employee_id = fields.Many2one('hr.employee', string="Instructor Name")
    start_date = fields.Datetime(required=True)
    end_date = fields.Datetime(required=True)
    duration = fields.Integer(required=True)
    is_mon = fields.Boolean(default=False)
    is_tue = fields.Boolean(default=False)
    is_wed = fields.Boolean(default=False)
    is_thu = fields.Boolean(default=False)
    is_fri = fields.Boolean(default=False)
    is_sat = fields.Boolean(default=False)
    is_sun = fields.Boolean(default=False)
    is_in_person = fields.Boolean(default=False)
    is_online = fields.Boolean(default=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ], default='draft')

    def action_draft(self):
        self.state = 'draft'

    def action_available(self):
        self.state = 'available'

    def action_not_available(self):
        self.state = 'not_available'
