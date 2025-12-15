from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(readonly=True)
    date_of_birth = fields.Date()


    @api.onchange('date_of_birth')
    def _onchange_date_of_birth(self):
        if self.date_of_birth:
            today = fields.Date.today()
            dob = fields.Date.from_string(self.date_of_birth)

            self.age = (
                today.year
                - dob.year
                - ((today.month, today.day) < (dob.month, dob.day))
            )
        else:
            self.age = 0


    total_class = fields.Integer(compute='_compute_total_class')

    def _compute_total_class(self):
        for record in self:
            all_class =self.env['ica.class.student'].search([('partner_id','=',record.id)]).mapped('class_id')
            record.total_class = len(all_class)


    def action_view_class(self):
        all_class = self.env['ica.class.student'].search([('partner_id', '=', self.id)]).mapped('class_id')
        return {
            "name":f"{self.name}'s classes",
            "type":"ir.actions.act_window",
            "res_model":"ica.class",
            "domain":[('id','in',all_class.ids)],
            "view_mode":"list,form",
            # "target":"fullscreen",
            # "target":"current", # default
            # "target":"main",
            "target":"new",
        }