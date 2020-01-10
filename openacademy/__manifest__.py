# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage Training""",

    'description': """
        Open Academy for managing training:
        - training courses
        - training sessions
        - attendees registrations
    """,

    'author': "Amberisk Consulting Limited",
    'website': "https://amberisk.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
