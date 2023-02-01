from odoo import models, fields, api
from odoo import tools


class AcademyReportTable(models.Model):
    _name = 'academy.report.table'
    _description = 'Academy Report Table'
    _auto = False

    enrollment_id = fields.Many2one('education.enrollment', readonly=True)
    student_id = fields.Many2one('education.student', readonly=True)
    class_id = fields.Many2one('education.class', readonly=True)
    student_ethnic_id = fields.Many2one('res.ethnic', readonly=True)
    student_country_id = fields.Many2one('res.country')
    date = fields.Date(string='Enroll Date', readonly=True)
    start_date = fields.Date(string='Start Date', readonly=True)
    end_date = fields.Date(string='End Date', readonly=True)
    

    def _select(self):
        return """
        SELECT enrollment.id AS id,
            student.id AS student_id,
            class.id AS class_id,
            enrollment.date AS date,
            class.start_date AS start_date,
            class.end_date AS end_date,
            eth.id AS student_ethnic_id,
            c.id AS student_country_id
        """
    
    def _from(self):
        return """
        FROM education_enrollment enrollment
            JOIN education_student student ON enrollment.student_id = student.id
            JOIN education_class class ON enrollment.class_id = class.id
            LEFT JOIN res_ethnic eth ON eth.id = student.ethnic_id
            LEFT JOIN res_country c ON c.id =  student.country_id
        """

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)

        self.env.cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                %s
                %s
            )
        """ % (self._table, self._select(), self._from())
                            )