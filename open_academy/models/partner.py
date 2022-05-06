# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string="Instructor", default=False)
    session_list = fields.Many2many(comodel_name="open_academy.session",
                                    relation="instructor_session_rel",
                                    column1="session_id",
                                    column2="partner_id",
                                    string="Sessions",
                                    readonly=True)
    category = fields.Selection(selection = [('teacher1', 'Teacher / Level 1'),
                                             ('teacher2', 'Teacher / Level 2')],
                                    string='Category',
                                    #compute = "_compute_company_type",
                                    #inverse = "_write_company_type"
                                    #default = 'none'
                                    )
    #@api.depends('is_company')
    #def _compute_company_type(self):
    #    for partner in self:
    #        partner.company_type = 'company' if partner.is_company else partner.company_type

    #def _write_company_type(self):
    #    for partner in self:
    #        partner.is_company = partner.company_type == 'company'

    #@api.onchange('company_type')
    #def onchange_company_type(self):
    #    self.is_company = (self.company_type == 'company')

    pass