from odoo import api, fields, models, tools
from odoo.exceptions import UserError


class SaleOrderAdditionalPage(models.Model):
    _name = "sale.order.additional.page"
    _inherit = ["mail.render.mixin"]
    _description = "Sale Order Additional Page"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    description_html = fields.Html(
        string="Description",
        render_engine="qweb",
        translate=True,
        sanitize=False,
    )
    type = fields.Selection(
        selection=[("first", "First"), ("last", "Last")],
        required=True,
        help="Use 'First' if you want the template to come before the sales "
        "report.\nUse 'Last' if you want the template to come after the sales "
        "report.",
    )
    sample_sale_id = fields.Many2one(
        comodel_name="sale.order",
        string="Sample Sale",
    )
    preview_html = fields.Html(
        string="Preview",
        compute="_compute_preview_html",
        sanitize=False,
    )

    def name_get(self):
        res = []
        for rec in self:
            name = rec.name
            if rec.type:
                name = "%s (%s)" % (name, rec.type)
            res.append((rec.id, name))
        return res

    @api.depends("sample_sale_id")
    def _compute_preview_html(self):
        for rec in self:
            rec.preview_html = self.with_context(
                sale=rec.sample_sale_id.id
            )._get_rendered_additional_page()

    def _get_rendered_additional_page(self):
        sale_id = self.env.context.get("sale", False)
        if not sale_id:
            return "You must select a sales order to display the content."
        try:
            sale = self.env["sale.order"].browse(sale_id)
            rendered = self._render_template_qweb(
                self.description_html,
                sale._name,
                [sale.id],
                add_context=None,
                options=None,
            )
            rendered = self._render_template_postprocess(rendered)
            return tools.html_sanitize(rendered[sale_id])
        except UserError as user_error:
            return user_error.args[0]
