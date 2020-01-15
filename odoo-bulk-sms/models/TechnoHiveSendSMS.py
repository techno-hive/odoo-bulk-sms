#-*- coding:utf-8 -*-

from odoo import models,fields

class TechnoHiveSendSMS(models.Model):
    _name='technohive.sendsms'
    phone_number=fields.Many2many('technohive.contact', string="Phone numbers",required="True")
    text_message=fields.Text(string="Message", required="True")
    state=fields.Selection([
        ('draft','Draft'),
        ('sent','Sent')
    ],required="True", default='draft')

    def btn_sendsms(self):
        print(self)
        for f in self.phone_number:
            print(f.phone_number)
            print(self.text_message)