from odoo import models, fields


class LmsResult(models.Model):
    _name = 'lms.result'
    _description = 'LMS Quiz Result'

    student_id = fields.Many2one('lms.student', string='Student', required=True)
    quiz_id = fields.Many2one('lms.quiz', string='Quiz', required=True)
    score = fields.Float(string='Score')
    state = fields.Selection([('draft','Draft'),('done','Done')], default='draft')
    taken_on = fields.Datetime(string='Taken On')
