# -*- coding: utf-8 -*-

from odoo import models, fields

class Wizard(models.TransientModel):

    _name = "open_academy.wizard"
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    #def _default_session(self):
    #    return self.env['open_academy.session'].browse(self._context.get('active_id'))

    def _default_sessions(self):
            return self.env['open_academy.session'].browse(self._context.get('active_ids'))


    #session_id = fields.Many2one("open_academy.session", string="Session", required=True, default=_default_session)
    session_list = fields.Many2many("open_academy.session", string="Sessions", required=True, default=_default_sessions)
    attendees_list = fields.Many2many("res.partner", string="Attendees")

    def subscribe(self):
        for session in self.session_list:
            session.attendees_list |= self.attendees_list
        #self.session_id.attendees_list |= self.attendees_list
        return {}

    pass
