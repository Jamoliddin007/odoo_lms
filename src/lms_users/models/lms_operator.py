from odoo import models, fields


class LmsOperator(models.Model):
    _name = 'lms.operator'
    _description = 'LMS Operator Profile'
    _inherits = {'res.users': 'user_id'}

    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='cascade')
    branch_id = fields.Many2one('lms.branch', string='Branch')
    shift = fields.Selection([('morning', 'Morning'), ('evening', 'Evening')], string='Shift', default='morning')
    position = fields.Char(string='Position', default='Operator')
    is_active = fields.Boolean(string='Active', default=True)
