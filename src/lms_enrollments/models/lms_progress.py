from odoo import models, fields


class LmsProgress(models.Model):
    _name = 'lms.progress'
    _description = 'Progress per student per course/module/lesson'

    enrollment_id = fields.Many2one('lms.enrollment', string='Enrollment', required=True, ondelete='cascade')
    lesson_id = fields.Many2one('lms.lesson', string='Lesson')
    completed = fields.Boolean(string='Completed', default=False)
    completion_date = fields.Date(string='Completion Date')
    percent = fields.Float(string='Percent Complete', default=0.0)
