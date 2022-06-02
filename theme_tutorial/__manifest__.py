# -*- coding: utf-8 -*-

{
    'name': "Tutorial Theme",
    'description': "This module is for learning theme development.",
    'version': "1.0",
    'author': "SNK",
    'category': "Theme/Creative",

    # 'depends': ['website', 'website_theme_install'],
    'depends': ['website'],

    'data': [
        # This option doesn't work.
        # 'views/assets.xml',
        'views/layout.xml',
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml',
    ],

    'assets': {
        # This option work.
        'web._assets_primary_variables': [
            'theme_tutorial/static/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            'theme_tutorial/static/src/scss/bootstrap_overridden.scss',
        ],
        'web.assets_frontend': [
            'theme_tutorial/static/scss/style.scss',
        ],
        'website.assets_editor': [
            'theme_tutorial/static/src/js/tutorial_editor.js',
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
