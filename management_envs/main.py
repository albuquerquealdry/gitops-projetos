import os 
import json

namespace = "prod"
component = "microservices"
service = "RAP_API"

def cloneCatalog():
    os.system("git clone https://github.com/albuquerquealdry/env-catalog.git") 
    with open(f"env-catalog/{component}.json", "r") as catalogEnvs:
        return json.load(catalogEnvs)

def checkEnvs():
    with open (".env", "r") as env:
        return (env.readlines())

def synchronize():
    getEnvs = cloneCatalog()
    envs = checkEnvs()
    os.system("cp -f files/configmapBase.yaml configmap.yaml")
    for env in envs:
        env = env.replace('\n',"")
        valuesEnv = getEnvs[f"{env}"]
        envForEnv = valuesEnv[f"{namespace}"]
        data = (f"""{env} : "{envForEnv}" """)
        os.system(f""" echo "\t{data}" >> configmap.yaml """)
        os.system(f""" sed -i "s/NAMESERVICE/{service}/g" configmap.yaml """)
        os.system("rm -rf env-catalog ")

sicronizer()
