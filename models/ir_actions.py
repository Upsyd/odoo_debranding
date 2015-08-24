# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2015-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
##############################################################################

from openerp import api, models, fields
from openerp.tools.translate import _


class ir_actions_act_window_debranding(models.Model):
    _inherit = 'ir.actions.act_window'

    def read(self, cr, uid, ids, fields=None,
             context=None, load='_classic_read'):
        results = super(ir_actions_act_window_debranding, self).read(
            cr, uid, ids, fields=fields, context=context, load=load)
        if not fields or 'help' in fields:
            new_name = self.pool.get('ir.config_parameter').get_param(
                cr, uid, 'odoo_debranding.new_name', False, context)
            new_name = new_name and new_name.strip() or _('Software')
            for res in results:
                if type(res) is dict and res.get('help'):
                    res['help'] = res['help'].replace('Odoo', new_name)
        return results

ir_actions_act_window_debranding()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
