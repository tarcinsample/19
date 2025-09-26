# -*- coding: utf-8 -*-

from odoo import models, fields

class AttendeeWizard(models.TransientModel):
    _name = 'op.attendee.wizard'
    _description = 'Attendee Wizard'

    session_id = fields.Many2one('op.session', string='Session', required=True)
    attendee_ids = fields.Many2many('op.student', string="Attendees")

    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {}