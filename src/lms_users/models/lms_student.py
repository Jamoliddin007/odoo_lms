from odoo import models, fields


class LmsStudent(models.Model):
    _name = 'lms.student'
    _description = 'LMS Student Profile'
    _inherits = {'res.users': 'user_id'}

    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='cascade')
    enrollment_date = fields.Date(string='Enrollment Date')
    group_id = fields.Many2one('lms.group', string='Group')
    course_ids = fields.Many2many('lms.course', string='Enrolled Courses')
    guardian_name = fields.Char(string='Guardian Name')
    guardian_phone = fields.Char(string='Guardian Phone')
    is_active = fields.Boolean(string='Active', default=True)
