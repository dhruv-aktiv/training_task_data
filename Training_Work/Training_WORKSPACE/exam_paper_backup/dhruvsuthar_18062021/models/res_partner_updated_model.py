from odoo import models, fields, api
from odoo.osv import expression


class ResPartnerU(models.Model):

    _inherit = "res.partner"

    def name_get(self):
        name_list = []
        for rec in self:
            name = f"{rec.name} ({rec.city})"
            name_list.append((rec.id, name))
        return name_list

    @api.model
    def _name_search(
        self, name="", args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        args = args or []
        domain = [("city", "ilike", name)]
        return self._search(expression.AND([domain, args]), limit=limit)
