from odoo import models, fields


class LmsQuestion(models.Model):
    _name = 'lms.question'
    _description = 'LMS Question'

    quiz_id = fields.Many2one('lms.quiz', string='Quiz', required=True, ondelete='cascade')
    text = fields.Text(string='Question Text', required=True)
    type = fields.Selection([('mcq','Multiple Choice'), ('text','Text Answer')], default='mcq', string='Type')
    option_ids = fields.One2many('lms.question.option', 'question_id', string='Options')
    correct_option_id = fields.Many2one('lms.question.option', string='Correct Option')
