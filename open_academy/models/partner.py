# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string="Instructor", default=False)
    session_ids = fields.Many2many(comodel_name="open_academy.session",
                                   relation="partner_session_rel",
                                   column1="session_id",
                                   column2="partner_id",
                                   string="Sessions",
                                   readonly=True)
    category = fields.Selection(selection=[('teacher1', 'Teacher / Level 1'),
                                           ('teacher2', 'Teacher / Level 2')],
                                string='Category')

    pass
