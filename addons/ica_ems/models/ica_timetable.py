from odoo import api, fields, models


class IcaClass(models.Model):
    _name = 'ica.timetable'
    _description = 'Ica Timetable'
    _rec_name = 'class_id'

    class_id = fields.Many2one('ica.class',required=True)
    start_datetime = fields.Datetime(required=True)
    end_datetime = fields.Datetime(required=True)
