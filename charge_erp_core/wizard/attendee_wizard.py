# -*- coding: utf-8 -*-

from odoo import _, models, fields
from odoo.exceptions import ValidationError

class AttendeeWizard(models.TransientModel):
    _name = 'op.attendee.wizard'
    _description = 'Attendee Wizard'

    session_id = fields.Many2one(
        'op.session', string='Session', required=True,
        default=lambda self: self.env.context.get('default_session_id'))
    attendee_ids = fields.Many2many('op.student', string="Attendees")

    def subscribe(self):
        if self.session_id.seats < len(self.attendee_ids) + len(self.session_id.attendee_ids):
            raise ValidationError(
                _("There are not enough seats for all the selected attendees."))
        self.session_id.attendee_ids |= self.attendee_ids
        return {}