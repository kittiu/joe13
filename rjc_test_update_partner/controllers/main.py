# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class PartnerUpdate(http.Controller):

    @route('/update_partner_name/<int:partner_id>/<string:partner_name>', type='http', auth="public")
    def update_partner_something(self, partner_id, partner_name):
        partner_sudo = request.env['res.partner'].sudo().browse(partner_id)
        old_name = partner_sudo.name
        partner_sudo.write({"name": partner_name})
        return str({"partner_id": partner_id, "old_name": old_name, "new_name": partner_name})
