# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import api, exceptions, fields, models, _


class Session(models.Model):
    _name = 'open_academy.session'
    _description = "Open Academy Session"
    _rec_name = 'name'

    name = fields.Char(string="Title", required=True, translate=True)
    start_date = fields.Date(string="Start Date", default=fields.datetime.today())
    duration = fields.Integer(string="Duration in day", default=1)
    end_date = fields.Date(string="End Date", compute='_compute_end_date')
    seats = fields.Integer(string="Number of seats")
    taken_seats = fields.Float(digits=(6, 2), string="Taken seats", compute='_compute_taken_seats')
    instructor_id = fields.Many2one(comodel_name="res.partner",
                                    string="Instructor",
                                    ondelete="set null",
                                    index=True,
                                    domain=['|',
                                            ('instructor', '=', True),
                                            '|',
                                            ('category', '=', 'teacher1'),
                                            ('category', '=', 'teacher2')]
                                    )
    attendees_ids = fields.Many2many(comodel_name="res.partner",
                                     relation="partner_session_rel",
                                     column1="partner_id",
                                     column2="session_id",
                                     string="Attendees"
                                     )

    course_id = fields.Many2one(comodel_name="open_academy.course", string="Course", ondelete="set null", index=True)
    active = fields.Boolean(default="True")
    color = fields.Integer()

    @api.onchange('seats')
    def _onchange_seats(self):
        if self.seats < 0:
            self.seats = 0
            return {
                'warning': {
                    'title': _("Error"),
                    'message': _("Number of seats cannot be negative.")
                }
            }
        pass

    @api.onchange('attendees_ids')
    def _onchange_attendees_ids(self):
        if len(self.attendees_ids) > self.seats:
            return {
                'warning': {
                    'title': _("Error"),
                    'message': _("The number of attendees cannot exceed the number of seats.")
                }
            }
        pass

    @api.depends('seats', 'attendees_ids')
    def _compute_taken_seats(self):
        for record in self:
            if record.seats != 0:
                record.taken_seats = 100.0 * len(record.attendees_ids) / record.seats
                pass
            else:
                record.taken_seats = 0.0
                pass
            pass
        pass

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            record.end_date = record.start_date + timedelta(days=record.duration)
            pass
        pass

    @api.constrains('instructor_id', 'attendees_ids')
    def _check_instructor_id(self):
        # for record in self:
        if self.instructor_id and not (self.instructor_id in self.attendees_ids):
            raise exceptions.ValidationError(_("The instructor is not present in the list of attendees."))
        pass

    pass
