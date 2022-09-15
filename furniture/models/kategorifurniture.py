from odoo import api, fields, models


class kategoriFurniture(models.Model):
    _name = 'furniture.kategorifurniture'
    _description = 'New Description'

    name = fields.Selection([('kursi', 'Kursi'),
                             ('meja', 'Meja'),
                             ('sofa', 'Sofa'),
                             ('lemari', 'Lemari'), 
                             ('furnitureoutdoor', 'Furniture Outdoor'),
                             ('lampu', 'Lampu'),
                             ('loker', 'Loker'),
                             ('furnituranakdanbayi', 'Furniture Anak dan Bayi')], 
                             string='Nama Kategori')

    # name = fields.Char(string='Nama kategori Furniture')
    kode_kelompok = fields.Char(string='Kode kategori Furniture')
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'kursi'):
            self.kode_kelompok = 'kur00'
        elif (self.name == 'meja'):
            self.kode_kelompok = 'mej00'
        elif (self.name == 'sofa'):
            self.kode_kelompok = 'sof00'
        elif (self.name == 'lemari'):
            self.kode_kelompok = 'lem00'
        elif (self.name == 'furnitureoutdoor'):
            self.kode_kelompok = 'furd00'
        elif (self.name == 'lampu'):
            self.kode_kelompok = 'lam00'
        elif (self.name == 'loker'):
            self.kode_kelompok = 'lok00'
        elif (self.name == 'furnituranakdanbayi'):
            self.kode_kelompok = 'furb00'

    kode_rak= fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='furniture.barang',
		                                inverse_name='kategorifurniture_id',
		                                string='Daftar Furniture')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['furniture.barang'].search([('kategorifurniture_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a

    daftar = fields.Char(string='Daftar Barang')
