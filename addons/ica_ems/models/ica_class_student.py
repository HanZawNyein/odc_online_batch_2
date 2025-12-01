from datetime import timedelta

from odoo import api, fields, models,_


class IcaClassStudent(models.Model):
    _name = 'ica.class.student'
    _description = 'IcaClass'


    partner_id = fields.Many2one('res.partner')
    class_id = fields.Many2one('ica.class.student')
