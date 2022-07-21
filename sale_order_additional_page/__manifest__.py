{
    "name": "Sale Order Additional Page",
    "summary": "Add additional pages in the sale report",
    "version": "15.0.1.0.0",
    "category": "Sales",
    "author": "Pegon, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/sale-reporting",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_additional_page_views.xml",
        "views/sale_order_views.xml",
        "report/sale_report_templates.xml",
    ],
    "installable": True,
}
