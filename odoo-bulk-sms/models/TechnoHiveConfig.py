#-*- coding:utf-8 -*-
from odoo import fields, models

class TechnoHiveConfig(models.Model):
    _name="technohive.config"
    _inherit = 'mail.thread'
    api_key=fields.Text(string="Api Key", required="True", placeholder="Get this from technohive site. http://technohive.co.ke")
    partner_id=fields.Char(string="Partner Id", placeholder="Get this from technohive site",required="True", track_visibilty="always")
    sender_id=fields.Char(string="Sender Id", placeholder="Get this from technohive website", required="True")
    state=fields.Selection([
        ('draft','Draft'),
        ('send','Sent'),
        ('cancel','Cancelled'),
    ],required=True, default='draft')

    def button_send(self):
        print("Josphat")