# -*- coding: utf-8 -*-
{
    "name": "FoodHub",
    "summary": """
        This is a Food Hub App """,
    "description": """
        Short description of module's purpose of Food Hub App
    """,
    "author": "Food Hub App Company",
    "website": "http://www.hospital_dt.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/foodhub_security.xml",
        "security/ir.model.access.csv",
        "food_item_detail.xml",
    ],
    # only loaded in demonstration mode
    "installable": True,
    "application": True,
    "auto_install": False,
}
