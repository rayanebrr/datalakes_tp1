import os
from azure.storage.filedatalake import DataLakeServiceClient



connection_string = "DefaultEndpointsProtocol=https;AccountName=csb10030000ad857dcd;AccountKey=Ucyanp3webafsocW1dBu7NC+2/BV9xR3vAXQVkArymz5iAy4ycHyOKI+IiIB3KQnvHEtyZDGBgSq+AStLaromg==;EndpointSuffix=core.windows.net"
datalake_service_client = DataLakeServiceClient.from_connection_string(connection_string)


def azure_up(dir, azure_directory=None):

    if(azure_directory):

        azure_directory = azure_directory + "/"

    else:

        azure_directory=""

    os.chdir(dir)
    
    for file in os.listdir(os.getcwd()):
        
        file_client = datalake_service_client.get_file_client(file_system_name, azure_directory + file)
        file_client.create_file()

        with open(file, 'rb') as f:

            file_content = f.read()
            file_client.append_data(data = file_content, offset=0, length=len(file_content))
            file_client.flush_data(len(file_content))
            
            
    os.chdir("..")
    print("uploaded successfully")



file_system_name = "datalake"
dirpath = "/Users/rayane/Downloads/data"


azure_up(dirpath)
