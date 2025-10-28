from odoo import models, fields


class LmsModule(models.Model):
    _name = 'lms.module'
    _description = 'LMS Module'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=1)
    description = fields.Text(string='Description')
    course_id = fields.Many2one('lms.course', string='Course', required=True)
    lesson_ids = fields.One2many('lms.lesson', 'module_id', string='Lessons')
