# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class OpAttendanceSheet(models.Model):
    _name = "op.attendance.sheet"
    _description = "Attendance Sheet"

    name = fields.Char('Name', required=True, default='New')
    batch_id = fields.Many2one('op.batch', 'Batch', required=True)
    subject_id = fields.Many2one('op.subject', 'Subject', required=True)
    faculty_id = fields.Many2one('op.faculty', 'Faculty', required=True)
    date = fields.Date('Date', required=True, default=fields.Date.today())
    attendance_line_ids = fields.One2many('op.attendance.line', 'sheet_id',
                                          string='Attendance Lines')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], 'State', default='draft', required=True)

    @api.onchange('batch_id')
    def _onchange_batch_id(self):
        self.attendance_line_ids = [(5, 0, 0)]
        if self.batch_id:
            student_list = []
            for student in self.batch_id.student_ids:
                student_list.append((0, 0, {'student_id': student.id}))
            self.attendance_line_ids = student_list

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('op.attendance.sheet') or 'New'
        return super(OpAttendanceSheet, self).create(vals)

    def action_start_attendance(self):
        self.state = 'in_progress'

    def action_mark_as_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_reset_to_draft(self):
        self.state = 'draft'
