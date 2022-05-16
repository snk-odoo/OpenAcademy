# -*- coding: utf-8 -*-
{

    'name': "Academy",
    
    'summary': "This module is for learning quest 3.",

    'description': """
    Very long description of module's purpose...
    """,

    'author': 'My company',
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'website', 'mail', 'website_sale'],
    #'depends': ['base', 'website', 'website_sale'],
    #'depends': ['base', 'website'],
    #'depends': ['mail', 'website_sale'],
    #'depends': ['website_sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/template.xml',
        'views/teachers.xml',
        #'views/courses.xml',
        'views/products.xml',
    ],

    'demo': [
        'demo/teachers.xml',
        'demo/courses.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 0,
    'license': 'LGPL-3',

}