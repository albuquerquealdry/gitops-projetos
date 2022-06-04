import os 
import json

component = "microservices"
def cloneCatalog():
    #os.system("git clone https://github.com/albuquerquealdry/env-catalog.git") 
    with open(f"env-catalog/{component}.json", "r") as catalogEnvs:
        return(catalogEnvs)
        
print(cloneCatalog())