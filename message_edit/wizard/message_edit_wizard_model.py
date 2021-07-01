
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class MessageNoteEdit(models.Model):
    _name = 'message.note.edit'
    _description = 'Message/Note Edit Wizard'

    author_id = fields.Many2one('res.partner', 'Author')
    email_from = fields.Char('From')
    message_id = fields.Many2one('mail.message')
    date = fields.Datetime()
    last_updated_date = fields.Datetime(default=fields.Datetime.now)
    related_document_model = fields.Char('Related Document')
    related_document_id = fields.Many2oneReference(
        'Related Document ID', index=True, model_field='related_document_model')
    message = fields.Html()
