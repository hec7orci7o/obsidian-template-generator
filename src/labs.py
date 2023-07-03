import os, argparse, paramiko
from pythonping import ping
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

USERNAME = os.getenv("NIP")
PASSWORD = os.getenv("PASSWORD")
PRIVATE_KEY = os.getenv("PRIVATE_KEY") if os.getenv("PRIVATE_KEY") != "" else None

LAB102 = [f"155.210.154.{ip}" for ip in range(191, 211)]
LAB104 = [f"10.3.17.{ip}" for ip in range(71, 101)]

def check_file(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        # Get the modification time of the file
        modification_time = os.path.getmtime(file_path)
        modification_datetime = datetime.fromtimestamp(modification_time)

        # Calculate the time difference
        current_datetime = datetime.now()
        time_difference = current_datetime - modification_datetime

        # Check if the file was modified more than 5 minutes ago
        if time_difference <= timedelta(minutes=5):
            # File was modified within the last 5 minutes
            print(f"File '{file_path}' was modified within the last 5 minutes. Exiting...")
            exit()

def write_header(file, header):
    # Escribe el encabezado de la tabla
    file.write("|" + "|".join(header) + "|\n")
    file.write("|" + "|".join(["---"] * len(header)) + "|\n")

    return file

def write_rows(file, lab):
    if lab == "Lab 1.02":
        lista_ips = LAB102
    elif lab == "Lab 1.04":
        lista_ips = LAB104

    for ip in lista_ips:
        end = ip.split(".")[-1]
        state, so = ping_host(ip)
        if state == "UP":   count = count_users_ssh(ip)
        else:               count = "---"

        data = ["{{domain}}", "{{ip}}", "{{state}}", "{{so}}", "{{num_users}}"]
        row = "|" + "|".join(data) + "|\n"
        row = row.replace("{{domain}}", f"lab102-{end}")
        row = row.replace("{{ip}}", ip)
        row = row.replace("{{state}}", tag(state, "green" if state == "UP" else "red"))
        row = row.replace("{{so}}", tag(so, "gray") if state == "UP" else "---") 
        row = row.replace("{{num_users}}", str(count))

        file.write(row)

def tag(text: str, color= "gray"):
    if color == 'green': 
        background  = 'rgba(16, 185, 129, 0.1)'
        border      = 'rgba(16, 185, 129, 0.2)'
        shadow      = 'rgba(16, 185, 129, 0.2)'
        color       = '#10B981'
    elif color == 'red':
        background  = 'rgba(185, 16, 16, 0.1)'
        border      = 'rgba(185, 16, 16, 0.2)'
        shadow      = 'rgba(185, 16, 16, 0.2)'
        color       = '#B91010'
    else: 
        background  = 'rgba(156, 163, 175, 0.1)'
        border      = 'rgba(156, 163, 175, 0.2)'
        shadow      = 'rgba(156, 163, 175, 0.2)'
        color       = '#9CA3AF'

    tag = f"<span style='display: inline-flex; align-items: center; border-radius: 0.375rem; background-color: {background}; padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.25rem; padding-bottom: 0.25rem; font-size: 0.75rem; font-weight: 500; color: {color}; border: 1px solid {border}; box-shadow: inset 0 1px 1px {shadow};'>{text}</span>"

    return tag

def ping_host(ip):
    try:
        response_list = ping(ip, count=1, timeout=1)
        ttl = response_list.rtt_avg_ms

        ttl = int(ttl)
            
        if ttl <= 64:
            return "UP", "Linux"
        elif ttl <= 128:
            return "UP", "Windows"
        elif ttl <= 255:
            return "UP", "---"
            
        return "DOWN", "---"
    
    except Exception:
        return "DOWN", "---"

def count_users_ssh(ip, ):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    count = -1

    try:
        if PRIVATE_KEY is not None:
            key = paramiko.Ed25519Key.from_private_key_file(PRIVATE_KEY)
            client.connect(ip, username=USERNAME, pkey=key, timeout=1)
        else:
            client.connect(ip, username=USERNAME, password=PASSWORD, timeout=1)
        
        _, stdout, _ = client.exec_command('who | wc -l')
        count = int(stdout.read().decode().strip())
    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {str(e)}")
    finally:
        client.close()

    return count

def main(VAULT_PATH, lab_name):
    lab_name = lab_name.capitalize().replace("Lab1", "Lab 1.")
    path = VAULT_PATH + lab_name + ".md"
    
    check_file(path)
    with open(path, "w", encoding="utf-8") as file:
        file.write("---\n")
        file.write("title: " + lab_name + "\n")
        file.write("date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write("---\n\n")

        file = write_header(file, header= ["name", "@ip", "state", "so", "numUsers"])
        write_rows(file, lab_name)
        file.close()

if __name__ == "__main__":
    try:
        # Crear el parser de argumentos
        parser = argparse.ArgumentParser(description='')
        parser.add_argument("-v", "--vault_path", help="Path of obsidian vault", required=True)
        parser.add_argument("-l", "--lab_name", help="Lab name", required=True)
        args = parser.parse_args()

        VAULT_PATH = args.vault_path
        lab_name = args.lab_name

        main(VAULT_PATH, lab_name)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)