# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - Present Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Redmine Connector',
    'version': '0.1',
    'author': 'Savoir-faire Linux,Odoo Community Association (OCA)',
    'maintainer': 'Odoo Community Association (OCA)',
    'website': 'http://odoo-community.org',
    'category': 'Connector',
    'description': """
Redmine Connector
=================
Add the Redmine Backend
""",
    'depends': [
        'connector',
        'hr_timesheet_sheet',
    ],
    'external_dependencies': {
        'python': ['redmine'],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/redmine_backend_view.xml',
        'views/redmine_menu.xml',
    ],
    'application': True,
    'installable': True,
    'active': False,
}
