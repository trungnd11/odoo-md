# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class OrderManagement(models.Model):
    _name = 'order.management'
    _rec_name = 'project_name'

    project_name = fields.Char(string='Tên dự án')
    customer = fields.Char(string='Tên Khách Hàng')
    site_id = fields.Many2one('site.management', string="Tên Công Trường")
    line_ids = fields.One2many('order.management.line', 'management_id', string='Chi tiết đơn hàng')
    total_qty_produced = fields.Integer(string='Tổng đã cấp', compute='_compute_qty')
    total_qty_remain = fields.Integer(string='Tổng chưa cấp', compute='_compute_qty')

    #hàm tính toán số lượng
    def _compute_qty(self):
        for record in self:
            if record.line_ids:
                total_produced = 0
                total_remain = 0
                for line_id in record.line_ids:
                    if line_id.quantity_produced:
                        total_produced += line_id.quantity_produced
                    if line_id.quantity_remain:
                        total_remain += line_id.quantity_remain
                record.total_qty_produced = total_produced
                record.total_qty_remain = total_remain
            else:
                record.total_qty_produced = 0
                record.total_qty_remain = 0

    def action_print_excel(self):
        url = self.env['ir.config_parameter'].sudo().get_param('web.base.url') + \
              "/order_management/static/Template_export.xlsx"
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'self',
            'res_id': self.id,
        }
class OrderManagementLine(models.Model):
    _name = 'order.management.line'

    product_id = fields.Many2one('product.product', string="Tên loại cọc")
    management_id = fields.Many2one('order.management', string="Quản lý đơn hàng")
    length = fields.Selection(string='Chiều dài',
                              selection=[('0', '6M'), ('1', '7M'), ('2', '8M'),
                                         ('3', '9M'), ('4', '10M'), ('5', '11M'),
                                         ('6', '12M'), ('7', '13M'), ('8', '14M')])
    type = fields.Selection(string='Loại', selection=[('0', 'Thân'), ('1', 'Mũi')])
    piece = fields.Integer(string="Đoạn")
    met = fields.Integer(string="m")
    contract = fields.Char(string='Hợp đồng')
    expected_date = fields.Date(string='Ngày dự kiến giao')
    quantity_produced = fields.Integer(string='SL đã sản xuất')
    quantity_remain = fields.Integer(string='SL chưa sản xuất')
    origin = fields.Char(string='Nguồn gốc')
