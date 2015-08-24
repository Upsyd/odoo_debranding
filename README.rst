Backend debranding
==================

Removes references to odoo.com:

1. Replaces "Odoo" in page title
2. Deletes Odoo label in footer
3. Deletes "Manage databases" link from login page
4. Deletes About Odoo link
5. Replaces default logo by empty image
6. Replaces "Odoo" in Dialog Box
7. Replaces default favicon to a custom one

By default the module replaces "Odoo" to "Software". To configure
module open Settings\\System Parameters and modify

* odoo_debranding.new_title (put space in value if you don't need Brand in Title)
* odoo_debranding.new_name
* odoo_debranding.favicon_url
