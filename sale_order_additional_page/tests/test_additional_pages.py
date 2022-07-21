import lxml.etree as etree

from odoo.modules.module import get_module_resource
from odoo.tests import common


class TestAdditionalPages(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.sale = self.env.ref("sale.sale_order_1")
        self.action_report = self.env.ref("sale.action_report_saleorder")
        self.first_page = self.env["sale.order.additional.page"].create(
            {
                "name": "Test First Page",
                "sequence": 10,
                "description_html": "<p>Portrait Sale Order <strong "
                "t-out='object.name or &quot;&quot;'>S00052</strong></p>",
                "type": "first",
            }
        )
        self.last_page = self.env["sale.order.additional.page"].create(
            {
                "name": "Test Last Page",
                "sequence": 10,
                "description_html": "<p>Contract Agreements <strong "
                "t-out='object.name or &quot;&quot;'>S00052</strong></p>",
                "type": "last",
            }
        )

    def test_sale_report_with_additional_pages(self):
        self.sale.additional_page_ids = [
            (6, 0, [self.first_page.id, self.last_page.id])
        ]

        file = open(
            get_module_resource(
                "sale_order_additional_page", "tests", "sale_report_demo.html"
            ),
            "rb",
        ).read()
        file_root = etree.fromstring(file, etree.HTMLParser())
        file_content = (
            etree.tostring(file_root, encoding="unicode", method="text")
            .replace("\n", "")
            .replace(" ", "")
        )

        html = self.action_report._render_qweb_html([self.sale.id])[0]
        html_root = etree.fromstring(html, etree.HTMLParser())
        html_content = (
            etree.tostring(html_root, encoding="unicode", method="text")
            .replace("\n", "")
            .replace(" ", "")
        )
        self.assertEqual(file_content, html_content)
