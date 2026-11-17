from odoo import models, fields


class Student(models.Model):
    _name = 'student'
    _description = 'Student Information'
    _log_access = False

    name = fields.Char(required=True)
    student_id = fields.Text()
    student_image =  fields.Text()