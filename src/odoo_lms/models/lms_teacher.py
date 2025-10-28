from odoo import models, fields


class Teacher(models.Model):
    _name = 'lms.teacher'
    _description = 'LMS Teacher'
    _inherits = {'res.users': 'user_id'}

    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='cascade')
    subject_ids = fields.Many2many('lms.subject', string='Subjects')
    specialization = fields.Char(string='Specialization')
    hire_date = fields.Date(string='Hire Date')
    salary = fields.Float(string='Salary')
    rating = fields.Float(string='Rating')
    is_active = fields.Boolean(string='Currently Teaching', default=True)
