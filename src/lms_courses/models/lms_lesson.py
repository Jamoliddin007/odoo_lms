from odoo import models, fields


class LmsLesson(models.Model):
    _name = 'lms.lesson'
    _description = 'LMS Lesson'

    name = fields.Char(string='Title', required=True)
    content = fields.Text(string='Content')
    module_id = fields.Many2one('lms.module', string='Module', required=True)
    video_url = fields.Char(string='Video URL')
    duration_min = fields.Integer(string='Duration (minutes)')
    sequence = fields.Integer(string='Sequence', default=1)
    active = fields.Boolean(default=True)
