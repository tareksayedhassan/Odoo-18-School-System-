{
    'name': 'School Management System',
    'version': '17.0.1.0.0',
    'summary': 'Custom Odoo module',
    'description': """
        Custom module for Odoo 17.
    """,
    'author': 'tarek elasyed',
    'website': 'https://ruknova.tech',
    'category': 'Custom',
    'license': 'LGPL-3',

    'depends': [
        'base',
    ],

    'data': [
    'security/ir.model.access.csv',

    ],

    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}