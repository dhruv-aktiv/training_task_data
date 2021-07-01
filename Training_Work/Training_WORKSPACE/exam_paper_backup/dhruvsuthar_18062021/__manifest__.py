# -*- coding: utf-8 -*-
{
    "name": "dhruvsuthar_18062021",
    "summary": """
       """,
    "description": """
        This module is related to sale order along with frontend.
    """,
    "author": "Aktiv Software",
    "website": "http://www.aktivsoftware.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management", "website"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/frontend/add_existing_check_order_menu.xml",
        "views/frontend/check_existing_order_view.xml",
        "views/frontend/list_of_sales_orders.xml",
        "views/frontend/sales_order_view.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        # 'demo/demo.xml',
    ],
    "installable": True,
    "application": True,
}
