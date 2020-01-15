#-*- coding:utf-8 -*-
from odoo import fields, models
import urllib3
import json

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

    def button_approve(self):
        print("work in progress")
        
        # http = urllib3.PoolManager()
        # URL = 'https://mysms.celcomafrica.com/api/services/sendsms/?apikey=" . urlencode($apikey) . "&partnerID=" . urlencode($partnerID) . "&message=" . urlencode($message) . "&shortcode=$shortcode&mobile=$mobile"'
        # root = '/notes/note'  # the path where the request handler is located
        # datas = http.request('GET', URL)
        # datas = json.loads(datas.data.decode('utf-8'))  # parses the response to  a compatible form
        # print(datas)
        # # for data in datas:
        # #     self.env['notes.note'].create({
        # #         'partner_id': self.env['res.partner.search'].search([('notes_user_id', '=', data['user_id'])]).id,
        # #         'note': data['note'],
        # #         'time_date': data['time']
        # #     })