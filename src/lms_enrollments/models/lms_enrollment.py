from odoo import models, fields


class LmsEnrollment(models.Model):
    _name = 'lms.enrollment'
    _description = 'Student Enrollment in Course'

    student_id = fields.Many2one('lms.student', string='Student', required=True, ondelete='cascade')
    course_id = fields.Many2one('lms.course', string='Course', required=True, ondelete='cascade')
    enrollment_date = fields.Date(string='Enrollment Date')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([('draft','Draft'),('active','Active'),('completed','Completed'),('cancelled','Cancelled')], default='draft', string='Status')
