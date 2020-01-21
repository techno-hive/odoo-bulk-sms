{
    'name':'TechnoHive Bulk SMS',
    'company':'TechnoHive Solutions',
    'author':'TechnoHive Solutions',
    'maintainer':'TechnoHive Solutions',
    'website':'https://technohive.co.ke',
    'summary':'Easily integrate bulk sms into odoo ERP System',
    'version':'12.0',
    'data':[
        'security/ir.model.access.csv',
        'views/technohive_config.xml',
        'views/technohive_contact.xml',
        'views/technohive_menu.xml',
        'views/technohive_sendsms.xml',
        'views/technohive_sentsms.xml',
    ],
    'depends':['base','mail'],
    'license':'AGPL-3',
}