from odoo import fields, models

class estate_property(models.Model):
    _name = 'estate_property'
    _description = 'Estate Module'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availabilitysel = fields.Date()
    expected_price = fields.Float(required=True)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north','North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
