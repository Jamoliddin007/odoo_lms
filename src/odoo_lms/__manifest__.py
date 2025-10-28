# -*- coding: utf-8 -*-
{
    'name': "odoo_lms",

    'summary': "Learning Management System for Odoo",

    'description': """
Odoo LMS — manage students, teachers, and operators efficiently.
    """,

    'author': "Jamoliddin",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        # Views (will be added later)
        # 'views/res_users_views.xml',
        # 'views/lms_student_views.xml',
        # 'views/lms_teacher_views.xml',
        # 'views/lms_operator_views.xml',
    ],

    'demo': [],
}
