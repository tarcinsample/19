# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentReportWizard(models.TransientModel):
    _name = 'student.report.wizard'
    _description = 'Student Report Wizard'

    course_id = fields.Many2one('op.course', string='Course', required=True)

    def action_print_report(self):
        students = self.env['op.student'].search([('batch_id.course_id', '=', self.course_id.id)])
        data = {
            'doc_ids': self.ids,
            'doc_model': self._name,
            'docs': self,
            'students': students,
            'course_name': self.course_id.name,
        }
        return self.env.ref('charge_erp_core.action_report_student_list').report_action(self, data=data)
