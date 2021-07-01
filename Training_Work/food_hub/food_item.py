from odoo import api, fields, models


class FoodItem(models.Model):
    _name = "food_hub.item.detail"
    _description = "food item detail"

    name = fields.Char(string="Item Name")
    qty = fields.Integer()
    price = fields.Float(digits=(10, 3))
