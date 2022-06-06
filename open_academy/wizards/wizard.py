# -*- coding: utf-8 -*-

from odoo import models, fields


class Wizard(models.TransientModel):

    _name = "open_academy.wizard"
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_sessions(self):
        return self.env['open_academy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many(comodel_name="open_academy.session",
                                   string="Sessions",
                                   required=True,
                                   default=_default_sessions)

    attendees_ids = fields.Many2many(comodel_name="res.partner", string="Attendees")

    def subscribe(self):
        for session in self.session_ids:
            session.attendees_ids |= self.attendees_ids
        return {}

    pass
