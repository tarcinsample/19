# -*- coding: utf-8 -*-
from odoo import models, fields

class OpStudent(models.Model):
    _name = 'op.student'
    _description = 'Student'
    _inherits = {'res.partner': 'partner_id'}

    # Link to res.partner
    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True, ondelete='cascade'
    )

    # Personal Information
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    birth_date = fields.Date(string='Birth Date')
    blood_group = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-')
    ], string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    visa_info = fields.Char(string='Visa Info')
    is_an_alumni = fields.Boolean(string='Is an Alumni?')

    # Contact Information
    mobile = fields.Char("Mobile")
    emergency_contact = fields.Char(string='Emergency Contact')

    # Other Information
    registration_number = fields.Char(string='Registration Number')
    library_card = fields.Char(string='Library Card')
    badge_id = fields.Char(string='Badge ID')
    category = fields.Char(string='Category')
    user_id = fields.Many2one('res.users', string='User')
    batch_id = fields.Many2one('op.batch', string='Batch')
    faculty_ids = fields.Many2many('op.faculty', string='Faculties')
    miscellaneous = fields.Text(string='Miscellaneous')

