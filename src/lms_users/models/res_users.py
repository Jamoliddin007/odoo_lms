from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'
    _description = 'Extend res.users for LMS'

    user_type = fields.Selection(
        [
            ('student', 'Student'),
            ('teacher', 'Teacher'),
            ('operator', 'Operator'),
            ('manager', 'Manager'),
            ('branch_manager', 'Branch Manager'),
            ('accountant', 'Accountant'),
            ('hr', 'HR'),
        ],
        string='User Type',
        default='student',
        index=True,
    )
    experience_year = fields.Integer(string='Experience (years)', default=0)
    work_places = fields.Char(string='Previous Work Places')
    passport_id = fields.Char(string='Passport / ID', copy=False)
    languages = fields.Many2many('res.lang', string='Languages Known')
    marital_status = fields.Selection(
        [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')],
        string='Marital Status'
    )
    children_count = fields.Integer(string='Children Count', default=0)
    phone_number = fields.Char(string='Phone Number')
    profile_image = fields.Binary(string='Profile Image')
    bio = fields.Text(string='Short Bio')
    joined_date = fields.Date(string='Joined Date')
    branch_id = fields.Many2one('lms.branch', string='Branch')
