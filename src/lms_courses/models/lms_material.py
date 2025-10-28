from odoo import models, fields


class LmsMaterial(models.Model):
    _name = 'lms.material'
    _description = 'LMS Material'

    name = fields.Char(string='Name', required=True)
    file = fields.Binary(string='File')
    filename = fields.Char(string='Filename')
    course_id = fields.Many2one('lms.course', string='Course')
    lesson_id = fields.Many2one('lms.lesson', string='Lesson')
    material_type = fields.Selection([('doc','Document'),('video','Video'),('link','Link')], string='Type')
