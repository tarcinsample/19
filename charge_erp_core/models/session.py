from odoo import models, fields

class Session(models.Model):
    _name = 'op.session'
    _description = 'Open Academy Sessions'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('op.faculty', string="Instructor")
    course_id = fields.Many2one('op.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('op.student', string="Attendees")
