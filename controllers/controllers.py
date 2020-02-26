# -*- coding: utf-8 -*-
from odoo import http

# class VitLocationSearch(http.Controller):
#     @http.route('/vit_location_search/vit_location_search/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_location_search/vit_location_search/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_location_search.listing', {
#             'root': '/vit_location_search/vit_location_search',
#             'objects': http.request.env['vit_location_search.vit_location_search'].search([]),
#         })

#     @http.route('/vit_location_search/vit_location_search/objects/<model("vit_location_search.vit_location_search"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_location_search.object', {
#             'object': obj
#         })