# -*- coding: utf-8 -*-

from odoo import models, fields


class Teachers(models.Model):

    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()
    #course_ids = fields.One2many(comodel_name='academy.courses', inverse_name='teacher_id', string="Courses")

    pass
