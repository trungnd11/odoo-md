# -*- coding: utf-8 -*-

from odoo import fields, models, _

class SiteManagement(models.Model):
    _name = 'site.management'
    _rec_name = 'name'

    name = fields.Char(string='Tên công trường')

    _sql_constraints = [
        ('name_unique', 'unique (name)', "Tên công trường này đã tồn tại"),
    ]