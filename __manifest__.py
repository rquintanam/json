{
	'name': "Invoice Fiscal Download Json",
	'version': '11.0.2.0.0',
	'category': '',
	'author': "Onedoos",
	'website': 'https://www.onedoos.com',
	'description': """
		Generate invoice json for panama fiscal printer
	""",
	'depends': ['account'],
	'data': [
		'views/account_invoice_view.xml',
		'views/res_config_settings_views.xml',
	],
	'installable': True,
	'application': True,
}
