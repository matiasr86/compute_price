
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    margin = fields.Float(string='Margen (%)', default=0.0)
    shipping_cost = fields.Float(string='Flete (%)', default=0.0)
    our_cost = fields.Float(string='Costo', default=0.0)

    @api.onchange('our_cost', 'margin', 'shipping_cost')
    def _compute_list_price(self):
        for product in self:
            product.list_price = product.our_cost * (1 + (product.margin / 100)) * (
                            1 + (product.shipping_cost / 100))


    @api.model
    def _initialize_our_cost(self):
        products = self.search([])
        for product in products:
            product.our_cost = product.standard_price / 1.03

