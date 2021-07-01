from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.http import request
from datetime import datetime


class CustomizedSaleOrderController(http.Controller):
    @http.route("/check-existing-order", type="http", auth="user", website=True)
    def portal_check_existing_order(self, **kw):
        if request.httprequest.method == "POST":
            return request.redirect(
                f"/sales-orders?start_date={kw['start_date']}&end_date={kw['end_date']}&status={kw['status']}"
            )

        return http.request.render("dhruvsuthar_18062021.portal_check_existing_order")

    @http.route("/sales-orders", type="http", auth="user", website=True)
    def portal_c_sales_orders(self, **kw):

        values = {}

        start_date = datetime.strptime(kw["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(kw["end_date"], "%Y-%m-%d")

        sales_orders = None

        if kw["status"] == "all":

            sales_orders = (
                request.env["sale.order"]
                .sudo()
                .search(
                    [("date_order", ">=", start_date), ("date_order", "<=", end_date)]
                )
            )
        else:

            sales_orders = (
                request.env["sale.order"]
                .sudo()
                .search(
                    [
                        ("date_order", ">=", start_date),
                        ("date_order", "<=", end_date),
                        ("state", "=", kw["status"]),
                    ]
                )
            )

        values.update({"sales_orders": sales_orders})
        return http.request.render("dhruvsuthar_18062021.portal_c_sales_order", values)

    @http.route(
        "/sales-orders/<int:sales_order_id>", type="http", auth="user", website=True
    )
    def portal_c_sales_order(self, sales_order_id, **kw):
        values = {}

        sales_order = request.env["sale.order"].sudo().browse([int(sales_order_id)])

        values.update({"sales_order": sales_order})

        return http.request.render(
            "dhruvsuthar_18062021.portal_c_s_sales_order", values
        )
