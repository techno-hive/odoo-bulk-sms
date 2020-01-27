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
        # when calling from another model, just call sendsms methods with arguments
        # e.g
        # self.sendsms("+254722549778","Hey TechnoHive Solutions. This module is wonderful")
        val=self.env['technohive.config'].search([])
        apikey=val.api_key
        partnerID=val.partner_id
        shortcode=val.sender_id
        message=self.text_message



        for f in self.phone_number:
            print(f)
            print("Hello world")
            http = urllib3.PoolManager()
            URL = "https://mysms.celcomafrica.com/api/services/sendsms/?apikey=" + apikey + "&partnerID=" + partnerID \
                  + "&message=" + message + "&shortcode="+ shortcode + "&mobile="+f.phone_number
            root = '/notes/note'  # the path where the request handler is located
            datas = http.request('GET', URL)

            decoded = json.loads(datas.data)

            print(decoded)

            if 'respose-code' in decoded:

            # if decoded['respose-code']:
                

                self.env['technohive_sentsms'].create({'message': self.text_message,'response_code':decoded['respose-code'],
                                                       'response_description':decoded['response-description'],
                                                       'mobile':f.phone_number})
            elif 'response-code' in decoded:
                print("Here")

                self.env['technohive_sentsms'].create({'message': self.text_message,'response_code':decoded['response-code'],
                                                       'response_description':decoded['response-description'],
                                                       'mobile':f.phone_number})

            else:

                # Access data SMS was sent

                for x in decoded['responses']:
                    print (x['respose-code'])
                    self.env['technohive_sentsms'].create({'message': self.text_message,'response_code':x['respose-code'],
                                                           'response_description':x['response-description'],
                                                           'mobile':f.phone_number,'message_id':x['messageid'],
                                                          'network_id': x['networkid']})

            # datas = json.loads(datas.data.decode('utf-8'))  # parses the response to  a compatible form
            # print(datas['responses'])

        self.write({'state': 'sent'})



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
        # print(datas.data)
        decoded = json.loads(datas.data)
        print("TechnoHive Solution")
        print(decoded)
        # print(decoded['respose-code'])
        if 'respose-code' in decoded:

            # if decoded['respose-code']:

            self.env['technohive_sentsms'].create(
                {'message': message, 'response_code': decoded['respose-code'],
                 'response_description': decoded['response-description'],
                 'mobile': phone})
        elif 'response-code' in decoded:

            self.env['technohive_sentsms'].create(
                {'message': message, 'response_code': decoded['response-code'],
                 'response_description': decoded['response-description'],
                 'mobile': phone})

        else:

            # Access data SMS was sent

            for x in decoded['responses']:
                print(x['respose-code'])
                self.env['technohive_sentsms'].create({'message': message, 'response_code': x['respose-code'],
                                                       'response_description': x['response-description'],
                                                       'mobile': phone,
                                                       'message_id': x['messageid'],
                                                       'network_id': x['networkid']})
