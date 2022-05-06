# -*- coding: utf-8 -*-

import random
from datetime import timedelta
from odoo import models, fields, api, exceptions, _
#form odoo.exceptions import ValidationError


# class open_academy(models.Model):
#    _name = 'open_academy.open_academy'
#    _description = 'OpenAcademy'
#
#    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text()
    cost = fields.Integer()
    const_bonus = fields.Float(string="Constant Bonus", compute='_compute_const_bonus')
    random_bonus = fields.Float(string="Randomize Bonus", compute='_compute_random_bonus')
    responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible", ondelete="set null", index=True)
    session_list = fields.One2many(comodel_name="open_academy.session", inverse_name="course_id")

    _sql_constraints = [
        ('name_description_check',
         'check (name != description)',
         _('The course name and description cannot be same.')),
        ('name_unique',
         'unique(name)',
         _('The course name should be unique.'))
    ]

    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count(
            [('name', '=like', _("Copy of {}%").format(self.name))]
        )
        if not copied_count:
            new_name = -("Copy of {}").format(self.name)
            pass
        else:
            new_name = _("Copy of {} ({})").format(self.name, copied_count)
            pass
        default["name"] = new_name
        return super(Course, self).copy(default)

    def _compute_random_bonus(self):
        for record in self:
            record.random_bonus = random.random()
            pass
        pass

    @api.depends('cost')
    def _compute_const_bonus(self):
        for record in self:
            # The bonus is 5% of the cost.
            record.const_bonus = record.cost * 0.05

    pass

class Session(models.Model):
    _name = 'open_academy.session'
    _description = "Open Academy Session"
    _rec_name = 'name'

    name = fields.Char(string="Title", required=True, translate=True)
    start_date = fields.Date(string="Start Date", default=fields.datetime.today())
    duration = fields.Integer(string="Duration in day", default=1)
    end_date = fields.Date(string="End Date", compute='_compute_end_date')
    seats = fields.Integer(string="Number of seats")
    taken_seats = fields.Float(digits=(6, 2),string="Taken seats", compute='_compute_taken_seats')
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
    attendees_list = fields.Many2many(comodel_name="res.partner",
                                       relation="instructor_session_rel",
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

    @api.onchange('attendees_list')
    def _onchange_attendees_list(self):
        if len(self.attendees_list) > self.seats:
            return {
                'warning': {
                    'title': _("Error"),
                    'message': _("The number of attendees cannot exceed the number of seats.")
                }
            }
        pass

    @api.depends('seats', 'attendees_list')
    def _compute_taken_seats(self):
        for record in self:
            if record.seats != 0:
                record.taken_seats = 100.0 * len(record.attendees_list) / record.seats
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

    @api.constrains('instructor_id', 'attendees_list')
    def _check_instructor_id(self):
        for record in self:
            if self.instructor_id and not self.instructor_id in self.attendees_list:
                raise exceptions.ValidationError(_("The instructor is not present in the list of attendees."))
        pass

    pass
