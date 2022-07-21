from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    additional_page_ids = fields.Many2many(
        comodel_name="sale.order.additional.page", string="Additional Pages"
    )
