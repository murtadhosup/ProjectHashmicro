# -*- coding: utf-8 -*-
# from odoo import http


# class Furniture(http.Controller):
#     @http.route('/furniture/furniture', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/furniture/furniture/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('furniture.listing', {
#             'root': '/furniture/furniture',
#             'objects': http.request.env['furniture.furniture'].search([]),
#         })

#     @http.route('/furniture/furniture/objects/<model("furniture.furniture"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('furniture.object', {
#             'object': obj
#         })

from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class furniture(http.Controller):
    @http.route('/furniture/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        # Mengambil semua barang dari table barang
        barang = request.env['furniture.barang'].search([])
        items = []

        for item in barang:
            items.append({
                'nama_barang': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

    @http.route('/furniture/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['furniture.supplier'].search([])
        items = []

        for item in supplier:
            items.append({
                'nama_perusahaan': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'barang_id': item.barang_id[0].name
            })
        
        return json.dumps(items)