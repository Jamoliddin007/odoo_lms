from odoo import models, fields

class LmsTeacher(models.Model):
    _name = 'lms.teacher'
    _inherits = {'res.users': 'user_id'}
    _description = 'LMS Teacher Profile'

    user_id = fields.Many2one('res.users', required=True, ondelete='cascade')
    subject_ids = fields.Many2many('lms.subject', string='Subjects')
    hire_date = fields.Date(string='Hire Date')
    salary = fields.Float(string='Salary')
    level = fields.Selection([
        ('junior', 'Junior Teacher'),
        ('middle', 'Middle Teacher'),
        ('senior', 'Senior Teacher'),
    ], string='Teacher Level')
