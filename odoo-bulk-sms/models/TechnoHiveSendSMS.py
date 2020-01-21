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
        # print(self)
        self.sendsms("+254713727937","Hey nigga")
        val=self.env['technohive.config'].search([])
        apikey=val.api_key
        partnerID=val.partner_id
        shortcode=val.sender_id
        message=self.text_message
        for f in self.phone_number:
            http = urllib3.PoolManager()
            URL = "https://mysms.celcomafrica.com/api/services/sendsms/?apikey=w" + apikey + "&partnerID=" + partnerID \
                  + "&message=" + message + "&shortcode="+ shortcode + "&mobile="+f.phone_number
            root = '/notes/note'  # the path where the request handler is located
            datas = http.request('GET', URL)
            # print(datas.data)
            decoded = json.loads(datas.data)
            print("TechnoHive Solution")
            print(decoded)
            # print(decoded['respose-code'])
            if 'respose-code' in decoded:
                print("hey nigga")
            # if decoded['respose-code']:
                print('incorrect spelling')
                self.env['technohive_sentsms'].create({'message': self.text_message,'response_code':decoded['respose-code'],
                                                       'response_description':decoded['response-description'],
                                                       'mobile':self.phone_number.phone_number})
            elif 'response-code' in decoded:
                print('correct spelling')
                self.env['technohive_sentsms'].create({'message': self.text_message,'response_code':decoded['response-code'],
                                                       'response_description':decoded['response-description'],
                                                       'mobile':self.phone_number.phone_number})

            else:

                # Access data SMS was sent
                for x in decoded['responses']:
                    print (x['respose-code'])
                    self.env['technohive_sentsms'].create({'message':'hey'})

            # datas = json.loads(datas.data.decode('utf-8'))  # parses the response to  a compatible form
            # print(datas['responses'])


    def sendsms(self,phone, message):
        val = self.env['technohive.config'].search([])


        apikey = val.api_key
        partnerID = val.partner_id
        shortcode = val.sender_id
        http = urllib3.PoolManager()
        URL = "https://mysms.celcomafrica.com/api/services/sendsms/?apikey=" + apikey + "&partnerID=" + partnerID \
              + "&message=" + message + "&shortcode=" + shortcode + "&mobile=" + phone
        root = '/notes/note'  # the path where the request handler is located
        datas = http.request('GET', URL)
        datas = json
