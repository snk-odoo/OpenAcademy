# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': 'The module is designed for learning',

    'description': """
        The module implemented tasks from quest 2 and refactored from quest 5.
    """,

    'author': "SNK",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'attachment_indexation'],

    # always loaded
    'data': [
        'security/open_academy_groups.xml',
        'security/open_academy_security.xml',
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/course_views.xml',
        'views/course_menus.xml',
        'views/session_views.xml',
        'views/session_menus.xml',
        'views/partner_views.xml',
        'views/partner_menus.xml',
        'views/wizard_views.xml',
        'views/wizard_menus.xml',
        'views/dashboard_views.xml',
        'views/dashboard_menus.xml',
        'reports/reports.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'data/course_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
