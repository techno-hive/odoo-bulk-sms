#-*- coding:utf-8 -*-

from odoo import models,fields
import urllib3
import json

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
        apikey="josphat"
        partnerID="josphat"
        shortcode="shortcode"
        message=self.text_message
        for f in self.phone_number:
            http = urllib3.PoolManager()
            URL = "https://mysms.celcomafrica.com/api/services/sendsms/?apikey=" + apikey + "&partnerID=" + partnerID \
                  + "&message=" + message + "&shortcode="+ shortcode + "&mobile="+f.phone_number
            root = '/notes/note'  # the path where the request handler is located
            datas = http.request('GET', URL + root)
            datas = json.loads(datas.data.decode('utf-8'))  # parses the response to  a compatible form
            print(datas)
            print(f.phone_number)
            print(self.text_message)