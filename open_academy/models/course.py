# -*- coding: utf-8 -*-

import random
from odoo import api, fields, models, _


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string="Title", required=True, translate=True)
    description = fields.Text()
    cost = fields.Integer()
    const_bonus = fields.Float(string="Constant Bonus", compute='_compute_const_bonus')
    random_bonus = fields.Float(string="Randomize Bonus", compute='_compute_random_bonus')
    responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible", ondelete="set null", index=True)
    session_ids = fields.One2many(comodel_name="open_academy.session", inverse_name="course_id")

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
            new_name = _("Copy of {}").format(self.name)
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
