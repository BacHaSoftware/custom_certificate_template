from odoo import api, exceptions, fields, models, _

class BHSSurvey(models.Model):
    _inherit = 'survey.survey'

    certification_report_layout = fields.Selection(selection_add=[('bhs_certificate', 'BHS Certificate')])