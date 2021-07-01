# -*- coding: utf-8 -*-
# Part of AktivSoftware See LICENSE file for full copyright
# and licensing details.
{
    'name': "Message/Note Edit",

    'summary': """
        The module will""",

    'description': """
        The module will """,

    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'version': '13.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'views/mail_templates_updated.xml',
        'views/mail_message_edit_view.xml'
    ],

    'images': [

    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/thread_update.xml',
    ]
}
