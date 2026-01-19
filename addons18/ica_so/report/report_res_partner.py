from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.ica_so.report_res_partner'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            x, y = 0, 0
            sheet.write(x, y, obj.name, bold)
            sheet.write(x, y+1, obj.phone)

            for so in obj.sale_order_ids:
                x+=1
                sheet.write(x, y, so.name)

                sheet.write(x, y+1, so.amount_total)
                sheet.write(x, y+2, so.currency_id.symbol)