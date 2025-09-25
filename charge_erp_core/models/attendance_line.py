# -*- coding: utf-8 -*-

from odoo import models, fields

class OpAttendanceLine(models.Model):
    _name = "op.attendance.line"
    _description = "Attendance Line"

    student_id = fields.Many2one('op.student', 'Student', required=True)
    sheet_id = fields.Many2one('op.attendance.sheet', 'Attendance Sheet', required=True, ondelete='cascade')
    present = fields.Boolean('Present', default=False)
