# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Task(models.Model):
    _inherit = 'project.task'

    colorpicker = fields.Char(
        string="Color Picker",
    )
