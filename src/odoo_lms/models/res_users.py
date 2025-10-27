from odoo import  models, fields, api
from odoo.exceptions import ValidationError
class ResUsers(models.Model):
    _inherit = 'res_users'
    _description = 'Extend res.users for LMS common fields'

user_type = fields.Selection(
    [
        ('student','Student'),
        ('teacher','Teacher'),
        ('operator', 'Operator'),
        ('manager', 'Manager'),
        ('branch_manager', 'Branch Manager'),
        ('accountant', 'Accountant'),
        ('hr', 'HR'),
    ]
    string='User Type',
    default='student',
    index=True,
    required=True,
help='Primary role used to control menus/views/behavior in LMS'
)
# HR / Profile fields
    experience_year = fields.Integer(string='Experience (years)', default=0)
    work_places = fields.Char(string='Previous Work Places', help='Comma-separated previous employers')
    passport_id = fields.Char(string='Passport / ID', copy=False, index=True)
    languages = fields.Many2many('res.lang', string='Languages Known', help='Languages the user speaks')
    marital_status = fields.Selection(
        [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')],
        string='Marital Status'
    )
    children_count = fields.Integer(string='Children Count', default=0)

    # Contact / profile
    phone_number = fields.Char(string='Phone Number')
    profile_image = fields.Binary(string='Profile Image')
    bio = fields.Text(string='Short Bio')
    joined_date = fields.Date(string='Joined Date')

    # Integration fields
    employee_id = fields.Many2one('hr.employee', string='Related Employee')
    branch_id = fields.Many2one('res.branch', string='Branch')

    _sql_constraints = [
        ('passport_unique', 'UNIQUE(passport_id)', 'Passport/ID must be unique.'),
    ]

    @api.constrains('experience_year', 'children_count')
    def _check_non_negative(self):
        for rec in self:
            if rec.experience_year is not None and rec.experience_year < 0:
                raise ValidationError("Experience years cannot be negative.")
            if rec.children_count is not None and rec.children_count < 0:
                raise ValidationError("Children count cannot be negative.")

    @api.onchange('user_type')
    def _onchange_user_type(self):
        # Example hook point: set some defaults for specific roles.
        # Keep minimal logic here; use automated server actions / cron or separate methods as needed.
        if self.user_type == 'operator':
            # placeholder for role-specific default adjustments
            pass
