# models/product.py
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    margin = fields.Float(related='product_tmpl_id.margin', readonly=False)
    shipping_cost = fields.Float(related='product_tmpl_id.shipping_cost', readonly=False)
    our_cost = fields.Float(related='product_tmpl_id.our_cost', readonly=False)

    @api.onchange('our_cost', 'margin', 'shipping_cost')
    def _compute_list_price_variant(self):
        for variant in self:
            if variant.margin > 0 and variant.shipping_cost > 0:
                variant.lst_price = variant.our_cost * (1 + (variant.margin / 100)) * (1 + (variant.shipping_cost / 100))
