import pandas as pd
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa

# Leer el archivo Excel
nombre_archivo_excel = r'C:\Desarrollos\Libro1.xlsx'  # Cambia esto al nombre de tu archivo Excel
df = pd.read_excel(nombre_archivo_excel)

# Carpeta de salida para los PDF individuales
carpeta_salida = 'pdf_individuales/'

# Cargar la plantilla HTML
template_loader = FileSystemLoader(searchpath="./")
template_env = Environment(loader=template_loader)
template = template_env.get_template('plantilla.html')

# Iterar a través de cada fila y generar un PDF individual
for i, row in df.iterrows():
    # Renderizar la plantilla con los datos de la fila actual
    html_content = template.render(
        invoice_id=row['Invoice ID'],
        branch=row['Branch'],
        city=row['City'],
        customer_type=row['Customer type'],
        gender=row['Gender'],
        product_line=row['Product line']
    )

    # Crear un archivo PDF individual
    nombre_archivo_pdf = f'{carpeta_salida}registro_{i + 1}.pdf'
    with open(nombre_archivo_pdf, "wb") as f:
        pisa.CreatePDF(html_content, dest=f)

    print(f'Se ha creado el archivo PDF: {nombre_archivo_pdf}')

print('Se han creado archivos PDF individuales para cada registro.')