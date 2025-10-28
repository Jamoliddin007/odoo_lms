from odoo import models, fields

class LmsStudent(models.Model):
    _name = 'lms.student'
    _inherits = {'res.users': 'user_id'}
    _description = 'LMS Student Profile'

    user_id = fields.Many2one('res.users', required=True, ondelete='cascade')
    enrollment_date = fields.Date(string='Enrollment Date')
    group_id = fields.Many2one('lms.group', string='Group')
    course_ids = fields.Many2many('lms.course', string='Courses')
    guardian_name = fields.Char(string='Guardian Name')
    guardian_phone = fields.Char(string='Guardian Phone')
