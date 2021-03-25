from docxtpl import DocxTemplate
from sql2json import run_query_by_name

if __name__ == '__main__':
    config = "config/db-config.json"

    invoice_template = 'config/templates/invoice-template.docx'

    my_query = """
    SELECT 'Empresa 1' AS customer_name, '001' AS invoice_number, NOW() AS date
    UNION ALL
    SELECT 'Empresa 2' AS customer_name, '002' AS invoice_number, NOW() AS date
    UNION ALL
    SELECT 'Empresa 3' AS customer_name, '003' AS invoice_number, NOW() AS date
    """

    customers_items = run_query_by_name(conection_name="mysql-local", query_name=my_query, config = config)

    for customer_item in customers_items:
        doc = DocxTemplate(invoice_template)
        context = customer_item
        doc.render(context)

        file_name = "output/{} - Invoice #{}.docx".format(customer_item["customer_name"], customer_item["invoice_number"])

        doc.save(file_name)

    print("DONE")

