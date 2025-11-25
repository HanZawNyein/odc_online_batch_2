from datetime import timedelta

from odoo import api, fields, models,_


class IcaClass(models.Model):
    _name = 'ica.class'
    _description = 'IcaClass'

    name = fields.Char(required=True)
    company_id = fields.Many2one('res.country', string="University Name")
    employee_id = fields.Many2one('hr.employee', string="Instructor Name")
    start_datetime = fields.Datetime(required=True)
    end_datetime = fields.Datetime(required=True)
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
    reference = fields.Char(default= lambda self:_("New"))

    timetable_ids = fields.One2many('ica.timetable', 'class_id', string="Timetables")

    @api.model
    def create(self, values):
        # Add code here
        for value in values:
            if value.get('reference',_('New')):
                value['reference']=self.env['ir.sequence'].next_by_code('ica.class')
        return super().create(values)

    def action_draft(self):
        self.state = 'draft'

    def action_available(self):
        self.state = 'available'

    def action_not_available(self):
        self.state = 'not_available'

    def action_generate_timetable(self):
        for rec in self:
            start_dt = rec.start_datetime
            end_dt = rec.end_datetime
            duration = rec.duration

            # Example boolean fields
            # rec.is_mon, rec.is_tue, rec.is_wed, rec.is_thu, rec.is_fri, rec.is_sat, rec.is_sun

            weekday_map = {
                0: rec.is_mon,
                1: rec.is_tue,
                2: rec.is_wed,
                3: rec.is_thu,
                4: rec.is_fri,
                5: rec.is_sat,
                6: rec.is_sun,
            }

            current_date = start_dt

            Timetable = self.env['ica.timetable']

            while current_date <= end_dt:
                weekday = current_date.weekday()  # Monday = 0

                if weekday_map.get(weekday):
                    # Create a record for this day
                    day_start = current_date
                    day_end = current_date + timedelta(hours=duration)

                    Timetable.create({
                        'class_id': rec.id,
                        'start_datetime': day_start,
                        'end_datetime': day_end,
                    })

                current_date += timedelta(days=1)

    def action_view_timetable(self):
        return {
            "type": "ir.actions.act_window",
            "name": f"{self.name}'s Timetable",
            "domain": [['id', 'in', self.timetable_ids.ids]],
            "view_mode": "list,form",
            "res_model": "ica.timetable",
        }
