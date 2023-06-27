import os, yaml, argparse
from hackthebox import HTBClient
from datetime import datetime
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')
STRUCTURE_CONF = os.environ.get('STRUCTURE_CONF')
FOLDER_TEMPLATE = os.environ.get('FOLDER_TEMPLATE')

print(STRUCTURE_CONF)

def get_machine(client):
    try:
        machine_data = client.do_request("GET", "/machine/profile/" + machine_name)
    except:
        machines = client.do_request("GET", "/sp/machines")
        machine_data = list(filter(lambda objeto: objeto['name'] == machine_name, machines))[0]
    
    matrix = client.do_request("GET", "/machine/graph/matrix/" + str(machine_data['id']))
    machine_data['matrix'] = matrix

    rating = client.do_request("GET", "/machine/graph/owns/difficulty/" + str(machine_data['id']))
    machine_data['rating'] = rating
    return machine_data

def generar_estructura(VAULT_PATH, machine_name):
    # Cargar la estructura desde un archivo YAML
    with open(STRUCTURE_CONF, 'r', encoding='utf-8') as archivo_yaml:
        datos_yaml = yaml.safe_load(archivo_yaml)
        archivo_yaml.close()

    generar_estructura_rec(json_data= datos_yaml, ruta_padre= VAULT_PATH, machine_name= machine_name)

def generar_estructura_rec(json_data, ruta_padre='', machine_name=''):
    for nombre, contenido in json_data.items():
        tipo = contenido['type']
        contenido.pop('type')
        ruta_actual = os.path.join(ruta_padre, nombre)
        if 'machine_name' in ruta_actual: 
            ruta_actual = ruta_actual.replace('machine_name', machine_name) 

        if tipo == 'file':
            # Leer contenido de la plantilla
            with open(FOLDER_TEMPLATE + '/' + contenido['template'], 'r', encoding='utf-8') as template:
                template_content = template.read()                
                template.close()

            # Copia de la plantilla
            with open(ruta_actual, 'w', encoding='utf-8') as f:
                f.write(template_content)
                f.close()

        elif tipo == 'directory':
            os.mkdir(ruta_actual)
            generar_estructura_rec(contenido, ruta_actual, machine_name)

def fill_template_info(template, data):
    try:    template = template.replace('{{name}}', data['name'])
    except: template = template.replace('{{name}}', '')

    try:    template = template.replace('{{avatar}}', data['avatar'])
    except: template = template.replace('{{avatar}}', '')

    try:    template = template.replace('{{difficultyText}}', data['difficultyText'])
    except: template = template.replace('{{difficultyText}}', 'Desconocida')

    try:    template = template.replace('{{os}}', data['os'])
    except: template = template.replace('{{os}}', 'Desconocido')

    try:    template = template.replace('{{ip}}', data['ip'])
    except: template = template.replace('{{ip}}', 'Desconectado')

    try:    template = template.replace('{{maker}}', str(list(data['matrix']['maker'].values())))
    except: template = template.replace('{{maker}}', '[0,0,0,0,0]')

    try:    template = template.replace('{{user}}',  str(list(data['matrix']['user'].values())))
    except: template = template.replace('{{user}}', '[0,0,0,0,0]')

    try:    
        # Convertir la fecha original a objeto datetime
        fecha_objeto = datetime.strptime(data['release'], "%Y-%m-%dT%H:%M:%S.%fZ")
        # Formatear la fecha en el formato deseado
        template = template.replace('{{release}}', fecha_objeto.strftime("%d de %B de %Y"))
    except: template = template.replace('{{release}}', 'DD de MM de YYYY')

    try:    
        users = [value["user"] for value in data['rating'].values()]
        template = template.replace('{{bar_user}}', str(users))
    except: 
        template = template.replace('{{bar_user}}', '[0,0,0,0,0,0,0,0,0,0]')

    try:    
        roots = [value["root"] for value in data['rating'].values()]
        template = template.replace('{{bar_root}}', str(roots))
    except: 
        template = template.replace('{{bar_root}}', '[0,0,0,0,0,0,0,0,0,0]')

    return template

def main(VAULT_PATH, machine_name):
    # Create an API connection
    client = HTBClient(app_token=API_TOKEN)
    
    # Get the machine data
    machine_data = get_machine(client)

    # Generate the folder structure
    generar_estructura(VAULT_PATH, machine_name)

    # Fill the templates
    for root, dirs, files in os.walk(VAULT_PATH):
        if machine_name + '.md' in files:
            path = os.path.join(root, machine_name+'.md')
            print(path)
            with open(path, 'r+', encoding='utf-8') as f:
                template = f.read()
                filled_template = fill_template_info(template, machine_data)
                f.seek(0)  # Colocar el puntero de lectura/escritura al principio del archivo
                f.write(filled_template)
                f.truncate()  # Truncar el archivo desde la posición actual si el nuevo contenido es más corto
                f.close()

if __name__ == "__main__":
    try:
        # Crear el parser de argumentos
        parser = argparse.ArgumentParser(description='HTB API Client for Obsidian')
        parser.add_argument("-v", "--vault_path", help="Path of obsidian vault", default="", required=True)
        parser.add_argument("-m", "--machine_name", help="Input of the machine", default="", required=False)
        args = parser.parse_args()

        VAULT_PATH = args.vault_path
        machine_name = args.machine_name

        main(VAULT_PATH, machine_name)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)