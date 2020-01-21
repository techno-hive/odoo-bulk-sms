#*-* coding:utf-8 -*-

from odoo import models, fields

class TechnoHiveSentSMS(models.Model):
    _name="technohive_sentsms"
    message=fields.Text()
    response_code=fields.Char(string="Response Code")
    response_description=fields.Char(string="Response Description")
    mobile=fields.Char(string="Mobile Number")
    message_id=fields.Char(string="Message ID")
    network_id=fields.Char(string="Network Id")






