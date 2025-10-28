from odoo import models, fields


class LmsBranch(models.Model):
    _name = 'lms.branch'
    _description = 'LMS Branch (location)'

    name = fields.Char(string='Branch Name', required=True)
    code = fields.Char(string='Code')
    company_id = fields.Many2one('res.company', string='Company')
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    phone = fields.Char(string='Phone')
    active = fields.Boolean(string='Active', default=True)
