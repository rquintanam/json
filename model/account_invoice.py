# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
import logging
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
import json

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
	_inherit='account.invoice'
			 
	@api.multi
	def generate_invoice_json(self):
		params = self.env['ir.config_parameter'].sudo()
		dir_json= params.get_param('invoice_fiscal_json.dir_json', default='') or ''
		
		data = {
			'data': {
				'head': [{
					'name': self.number,
					'seller': self.partner_id.name,
					'sellt': 'Credit',
					'total': str(self.amount_total),
					'subt': str(self.amount_untaxed),
					'tax': str(self.amount_tax),
					'ruc': self.name
				}],
				'data': []
			}
		}
		data_line = []
		for line in self.invoice_line_ids:
			taxp = 0
			mapped = line.invoice_line_tax_ids.mapped('amount')
			if mapped:
				taxp = mapped[0]
				
			data_line.append({
				'cod': line.product_id.name,
				'descr': line.name,
				'quant': line.quantity,	
				'price': line.price_unit,
				'taxp': taxp,
				'disc': 0,
				'total': (line.quantity * (line.price_unit - 0)),
				'imp': '',
				'id': str(line.id)
			})
			
		data['data']['data'] = data_line
		
		with open(dir_json + self.number.replace('/', '-') + '.json', 'w') as outfile:
			json.dump(data, outfile)
		
		
		
					