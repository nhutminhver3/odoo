from odoo import api, fields, models

class samsung_pro(models.Model):
    _name = "samsung_pro"
    _description = "Samsung Module"

    name = fields.Char(string='Name')
    deviceif = fields.Text()
    infomation_device = fields.Text()
    warranty = fields.Date()
    date_buy = fields.Date()
    cpuif = fields.Selection([('apple','Apple'), ('Huawei', 'Huawei'), ('usa', 'Usa'), ('china', ('China'))])
