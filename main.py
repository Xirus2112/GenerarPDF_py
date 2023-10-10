import pandas as pd
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa

# Leer el archivo Excel
#nombre_archivo_excel = r'C:\Desarrollos\Libro2.xlsx'  # Cambia esto al nombre de tu archivo Excel
#df = pd.read_excel(nombre_archivo_excel)

from sqlalchemy import create_engine

host = "localhost"
user = "root"
password = ""
database = "migracion_server"
tabla = "hhistorias"

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

consulta_sql = f'SELECT * FROM {tabla} WHERE id = 24'

df = pd.read_sql_query(consulta_sql, engine)

#ver = df.head()

engine.dispose()

# Carpeta de salida para los PDF individuales
carpeta_salida = 'pdf_individuales/'

# Cargar la plantilla HTML
template_loader = FileSystemLoader(searchpath="./")
template_env = Environment(loader=template_loader)
template = template_env.get_template('plantilla_tres.html')

# Iterar a través de cada fila y generar un PDF individual
for i, row in df.iterrows():
    num_dcto = documento=row['documento']
    num_historia = NoHistoria=row['NoHistoria']
    imagen = firma=row['firma']
    id = row['id']
    # Renderizar la plantilla con los datos de la fila actual
    html_content = template.render(
        NoHistoria=row['NoHistoria'],
        fecAtencion=row['fecAtencion'],
        No_Admision=row['No_Admision'],
        fIngreso=row['fIngreso'],
        fSalida=row['fSalida'],
        NombresPaciente = row['NombresPaciente'],
        documento=row['documento'],
        LugarNacimiento=row['LugarNacimiento'],
        Fnacimiento=row['Fnacimiento'],
        edad=row['edad'],
        EstadoCivil=row['EstadoCivil'],
        Sexo=row['Sexo'],
        Ciudad=row['Ciudad'],
        motivoConsulta=row['motivoConsulta'],
        EnfermedadActual=row['EnfermedadActual'],
        antecedentes=row['antecedentes'],
        Revision_Sistema=row['Revision_Sistema'],
        TA=row['TA'],
        pulso=row['pulso'],
        FR=row['FR'],
        temperatura=row['temperatura'],
        peso=row['peso'],
        talla=row['talla'],
        imc=row['imc'],
        pc=row['pc'],
        spo2=row['spo2'],
        scor=row['scor'],
        PerimetroBraquial=row['PerimetroBraquial'],
        frax=row['frax'],
        rcv=row['rcv'],
        edol=row['edol'],
        gw=row['gw'],
        pabd1=row['pabd1'],
        examen_fisico=row['examen_fisico'],
        dx1=row['dx1'],
        dx2=row['dx2'],
        ComentarioDx=row['ComentarioDx'],
        ExamenFisico=row['ExamenFisico'],
        Evaluacion=row['Evaluacion'],
        PlanDx=row['PlanDx'],
        Evolucion=row['Evolucion'],
        IdMedico=row['IdMedico'],
        CodEspecialidad=row['CodEspecialidad'],
        NombreMedico=row['NombreMedico'],
        Especialidad=row['Especialidad'],
        imagen=imagen
    )

    # Crear un archivo PDF individual
    #nombre_archivo_pdf = f'{carpeta_salida}{num_dcto}_{num_historia}_{i + 1}.pdf'
    nombre_archivo_pdf = f'{carpeta_salida}{num_dcto}_{id}_{i + 1}.pdf'
    with open(nombre_archivo_pdf, "wb") as f:
        pisa.CreatePDF(html_content, dest=f)

    print(f'Se ha creado el archivo PDF: {nombre_archivo_pdf}')
print("-------------------------------------------------------")
print("Proceso Terminado...")