# -*- coding: utf-8 -*-

from odoo import models, fields


class Courses(models.Model):

    # _name = 'academy.courses'
    # _inherit = ['mail.thread', 'product.template']
    _inherit = 'product.template'

    # name = fields.Char()
    teacher_id = fields.Many2one(comodel_name='academy.teachers', string="Teacher")

    pass
