from lib2to3.fixer_util import Comma

from odoo import api, fields, models


class IcaBookingWizard(models.TransientModel):
    _name = 'ica.booking.wizard'
    _description = 'IcaBookingWizard'

    partner_id = fields.Many2one('res.partner', required=True)
    user_id = fields.Many2one('res.users', readonly=True,default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company',readonly=True)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    fees = fields.Monetary(currency_field='currency_id')

    def action_add_students(self):
        ...
        self._add_students()

    def _add_students(self):
        context = self.env.context
        active_model = context.get('active_model')
        active_id = context.get('active_id')
        ica_class_id = self.env[active_model].browse(active_id)
        ica_class_id.student_ids = [(0,0,{'partner_id':self.partner_id.id})]
        # Command.link(company.id)
        # ica_class_id.student_ids = [Command.link(self.partner.id)]