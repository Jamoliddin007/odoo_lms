from odoo import models, fields


class LmsCourse(models.Model):
    _name = 'lms.course'
    _description = 'LMS Course'

    name = fields.Char(string='Title', required=True)
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')
    category_id = fields.Many2one('lms.category', string='Category')
    teacher_id = fields.Many2one('lms.teacher', string='Teacher')
    module_ids = fields.One2many('lms.module', 'course_id', string='Modules')
    price = fields.Float(string='Price')
    duration = fields.Integer(string='Duration (hours)')
    level = fields.Selection([('beginner','Beginner'), ('intermediate','Intermediate'), ('advanced','Advanced')], default='beginner', string='Level')
    active = fields.Boolean(default=True)
