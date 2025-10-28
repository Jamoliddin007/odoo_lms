from odoo import models, fields


class LmsQuiz(models.Model):
    _name = 'lms.quiz'
    _description = 'LMS Quiz / Exam'

    name = fields.Char(string='Title', required=True)
    course_id = fields.Many2one('lms.course', string='Course')
    lesson_id = fields.Many2one('lms.lesson', string='Lesson')
    question_ids = fields.One2many('lms.question', 'quiz_id', string='Questions')
    duration_min = fields.Integer(string='Duration (minutes)')
    passing_score = fields.Float(string='Passing Score')
