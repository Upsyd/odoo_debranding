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

import re
from openerp import SUPERUSER_ID, models, tools, api


class ir_translation(models.Model):
    _inherit = 'ir.translation'

    def _debrand(self, cr, uid, source):
        if not source or not re.search(r'\bodoo\b', source, re.IGNORECASE):
            return source

        new_name = self.pool['ir.config_parameter'].get_param(
            cr, SUPERUSER_ID, 'odoo_debranding.new_name', False)

        if not new_name:
            return source

        return re.sub(r'\bodoo\b', new_name, source, flags=re.IGNORECASE)

    @tools.ormcache(skiparg=3)
    def _get_source(self, cr, uid, name, types, lang,
                    source=None, res_id=None):
        res = super(ir_translation, self)._get_source(
            cr, uid, name, types, lang, source, res_id)
        return self._debrand(cr, uid, res)

ir_translation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
