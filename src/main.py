import os, yaml, argparse
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

DEGREE_PATH = os.environ.get('DEGREE_PATH')
STRUCTURE_CONF = os.environ.get('STRUCTURE_CONF')
FOLDER_TEMPLATE = os.environ.get('FOLDER_TEMPLATE')

CURSO = {
    1: 'Primero',
    2: 'Segundo',
    3: 'Tercero',
    4: 'Cuarto',
    5: 'Quinto',
    6: 'Sexto'
}

print(STRUCTURE_CONF)

def get_subject(subject_name: str):
    df = pd.read_excel(DEGREE_PATH, sheet_name='Merge')
    fila = df.loc[(df['Código'] == int(subject_name)) | (df['Nombre'] == str(subject_name))]
    fila = fila.to_dict('records')[0]

    try:
        tablas = pd.read_html("https://estudios.unizar.es/estudio/asignatura?anyo_academico=2023&asignatura_id={}&estudio_id=20230148&centro_id=110&plan_id_nk=439".format(str(fila['Código'])))
        tabla_profesores = tablas[0]
        profesores = tabla_profesores.loc[tabla_profesores[0] == 'Profesores'][1].values[0]
        profesores = [profesor.strip() for profesor in profesores.split(',')]

        fila['Profesores'] = profesores
    except:
        fila['Profesores'] = []

    return fila

def generar_estructura(VAULT_PATH, subject_name):
    # Cargar la estructura desde un archivo YAML
    with open(STRUCTURE_CONF, 'r', encoding='utf-8') as archivo_yaml:
        datos_yaml = yaml.safe_load(archivo_yaml)
        archivo_yaml.close()

    generar_estructura_rec(json_data= datos_yaml, ruta_padre= VAULT_PATH, subject_name= subject_name)

def generar_estructura_rec(json_data, ruta_padre='', subject_name=''):
    for nombre, contenido in json_data.items():
        tipo = contenido['type']
        contenido.pop('type')
        ruta_actual = os.path.join(ruta_padre, nombre)
        if 'subject_name' in ruta_actual: 
            ruta_actual = ruta_actual.replace('subject_name', subject_name) 

        if tipo == 'file':
            if not os.path.exists(ruta_actual + '.md'):
                # Leer contenido de la plantilla
                with open(FOLDER_TEMPLATE + '/' + contenido['template'], 'r', encoding='utf-8') as template:
                    template_content = template.read()                
                    template.close()

                # Copia de la plantilla
                with open(ruta_actual, 'w', encoding='utf-8') as f:
                    f.write(template_content)
                    f.close()

        elif tipo == 'directory':
            if not os.path.exists(ruta_actual):
                os.mkdir(ruta_actual)
                generar_estructura_rec(contenido, ruta_actual, subject_name)

def fill_subject(template, data):
    print(data['Código'], data['Curso'])

    try:    template = template.replace('{{Nombre}}', data['Nombre'])
    except: template = template.replace('{{Nombre}}', '')
    
    try:    template = template.replace('{{Código}}', str(data['Código']))
    except: template = template.replace('{{Código}}', '')

    try:    template = template.replace('{{Curso}}', CURSO[data['Curso']])
    except: template = template.replace('{{Curso}}', '')
        
    try:    template = template.replace('{{Periodo}}', data['Periodo'].capitalize())
    except: template = template.replace('{{Periodo}}', '')
        
    try:    template = template.replace('{{Carácter}}', data['Carácter'])
    except: template = template.replace('{{Carácter}}', '')
        
    try:    template = template.replace('{{Créditos}}', str(data['Créditos']))
    except: template = template.replace('{{Créditos}}', '')
    
    try:    template = template.replace('{{Plazas}}', str(data['Plazas']))
    except: template = template.replace('{{Plazas}}', '')
    
    try:    template = template.replace('{{Idioma}}', data['Idioma'])
    except: template = template.replace('{{Idioma}}', '')

    try:    
        profesores = ''
        for profesor in data['Profesores']:
            encodedTeacher = profesor.replace(' ', '%20')
            profesores += '- [' + profesor + '](https://directorio.unizar.es/#/personas?cadena=' + encodedTeacher + ')\n'
        template = template.replace('{{Profesores}}', profesores)
    except: template = template.replace('{{Profesores}}', '')

    template = template.replace('{{school_year}}', str(datetime.now().year))

    try:    template = template.replace('{{analysis_data_max}}', str(data['Matriculados']))
    except: template = template.replace('{{analysis_data_max}}', '')

    try:
        analysis_data = '[' + str(data['Aprobados']) + ',' + str(data['Suspensos']) + ',' + str(data['NoPresentados']) + ',' + str(data['Recu']) + ']'
        template = template.replace('{{analysis_data}}', analysis_data)
    except: 
        template = template.replace('{{analysis_data}}', '[0,0,0,0]')

    try:    
        distributed_data = '[' + str(data['MH']) + ',' + str(data['S']) + ',' + str(data['N']) + ',' + str(data['B']) + ',' + str(data['Suspensos']) + ',' + str(data['NoPresentados']) + ',' + str(data['O']) + ']'
        template = template.replace('{{distributed_data}}', distributed_data)
    except: 
        template = template.replace('{{distributed_data}}', '[0,0,0,0,0,0,0]')

    return template

def main(VAULT_PATH, subject_name):
    # Get the machine data
    subject_data = get_subject(subject_name)

    # Generate the folder structure
    generar_estructura(VAULT_PATH, subject_data['Nombre'])

    # Fill the templates
    for root, dirs, files in os.walk(VAULT_PATH):
        if subject_data['Nombre'] + '.md' in files:
            path = os.path.join(root, subject_data['Nombre'] + '.md')
            print(path)
            with open(path, 'r+', encoding='utf-8') as f:
                template = f.read()
                filled_template = fill_subject(template, subject_data)
                f.seek(0)  # Colocar el puntero de lectura/escritura al principio del archivo
                f.write(filled_template)
                f.truncate()  # Truncar el archivo desde la posición actual si el nuevo contenido es más corto
                f.close()

if __name__ == "__main__":
    try:
        # Crear el parser de argumentos
        parser = argparse.ArgumentParser(description='Generador de estructura de asignaturas')
        parser.add_argument("-v", "--vault_path", help="Path del vault de obsidian", required=True)
        parser.add_argument("-s", "--subject_name", help="Input of the subject", required=True)
        args = parser.parse_args()

        VAULT_PATH = args.vault_path
        subject_name = args.subject_name

        main(VAULT_PATH, subject_name)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)