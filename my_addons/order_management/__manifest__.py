# -*- coding: utf-8 -*-
{
    'name': 'Order Management',
    'version': '1.0',
    'category': 'Order',
    'summary': """
        Order Management
        """,
    'description': """ Order Management
    """,
    'author': "HUYNV",
    'website': 'https://www.odoo.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/order_management_view.xml',
        'views/site_management_view.xml',
    ],
    'css': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
