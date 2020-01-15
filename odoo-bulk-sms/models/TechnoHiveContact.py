# -*- coding:utf-8 *-*

from odoo import models, fields

class TechnoHiveContact(models.Model):
    _name="technohive.contact"
    _inherit="mail.thread"
    name=fields.Char(string="Name",required="True")
    phone_number=fields.Char('Phone Number', required="True",placeholder="Start with country code")
    description=fields.Text(string="Description", placeholder="Description about the customer")