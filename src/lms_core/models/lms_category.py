from odoo import models, fields


class LmsCategory(models.Model):
    _name = 'lms.category'
    _description = 'LMS Course Category'

    name = fields.Char(string='Name', required=True)
    parent_id = fields.Many2one('lms.category', string='Parent Category')
    child_ids = fields.One2many('lms.category', 'parent_id', string='Child Categories')
    description = fields.Text(string='Description')
