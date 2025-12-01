from odoo import api, fields, models,_
from odoo.exceptions import UserError


class IcaClass(models.Model):
    _name = 'ica.timetable'
    _description = 'Ica Timetable'
    _rec_name = 'class_id'

    class_id = fields.Many2one('ica.class', required=True)
    start_datetime = fields.Datetime(required=True)
    end_datetime = fields.Datetime(required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('started', 'Started'),
        ('finished', 'Finished'),
        ('cancelled', 'Cancelled'),
    ], default='draft')

    def action_finish(self):
        if self.start_datetime > fields.Datetime.now():
            raise UserError(_('The start date cannot be in the future.'))
        self.state = 'finished'

    def action_cancel(self):
        self.state = 'cancelled'

