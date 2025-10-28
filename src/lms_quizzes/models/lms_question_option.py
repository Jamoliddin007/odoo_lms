from odoo import models, fields


class LmsQuestionOption(models.Model):
    _name = 'lms.question.option'
    _description = 'LMS Question Option'

    question_id = fields.Many2one('lms.question', string='Question', required=True, ondelete='cascade')
    text = fields.Char(string='Option Text', required=True)
