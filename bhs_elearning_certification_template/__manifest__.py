# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Certificate Template',
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',
    'version': '1.0',
    'category': 'eLearning',
    'sequence': 101,
    'summary': 'Custom eLearning Certification Template',
    'description': "A product of Bac Ha Software provides additional options for certificate templates.",
    'images': ['static/description/banner.gif'],
    'depends': ['survey'],
    'data': [
        'views/survey_report_templates.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'bhs_elearning_certification_template/static/src/scss/survey_reports.scss',
        ],
    },
    'demo': [],
    "external_dependencies": {},
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    'license': 'LGPL-3'
}
