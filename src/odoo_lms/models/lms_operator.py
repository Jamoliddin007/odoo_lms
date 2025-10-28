from odoo import models, fields

class LmsOperator(models.Model):
    _name = 'lms.operator'
    _inherits = {'res.users': 'user_id'}
    _description = 'LMS Operator Profile'

    user_id = fields.Many2one('res.users', required=True, ondelete='cascade')
    branch_id = fields.Many2one('res.branch', string='Branch')
    shift = fields.Selection([
        ('morning', 'Morning'),
        ('evening', 'Evening'),
    ], string='Shift')
