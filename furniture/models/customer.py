from odoo import api, fields, models

class Customer(models.Model):
    _inherit = 'res.partner'
    _description = 'Contact'

    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')