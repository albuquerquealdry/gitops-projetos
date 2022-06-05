# gitops-projetos
## Voz de Deus : conhecerás o git, e o git te libertará.
---

# Gerenciamento de Envs por catálogo de envs:

O objetivo desse projeto é usar 100% o git para gerenciar os valores das variáveis de ambiente através de um script python:
![Captura de tela de 2022-06-04 23-09-39](https://user-images.githubusercontent.com/85401149/172031956-aff41a78-8bd0-407f-ba33-4040522c5c87.png)

## Funcionamento:
### Primeiro temos um repositório que contém as envs de todos os serviços que englobam o projeto:
![Captura de tela de 2022-06-04 23-13-32](https://user-images.githubusercontent.com/85401149/172032039-20f19735-680a-46f2-a750-745bf4726d16.png)

### Dentro dele temos um json com os objetos referente as envs e suas respectivas esteiras:
![Captura de tela de 2022-06-04 23-15-05](https://user-images.githubusercontent.com/85401149/172032072-74d388b9-e0c9-4cad-8c65-a40d789a4247.png)

### Agora o script python se encarega de pegar esse repositório e colher as envs dele:

#### Temos as envs do projeto dentro de um .env
![Captura de tela de 2022-06-04 23-16-57](https://user-images.githubusercontent.com/85401149/172032130-4ec8e624-197b-47b3-a824-ce432e106784.png)

#### Agora ao rodar o script Python, o mesmo pega as envs citadas em .env e faz gera o config map deacordo com o repositorio do catálogo de envs:
![Captura de tela de 2022-06-04 23-20-32](https://user-images.githubusercontent.com/85401149/172032193-a92d746f-44a6-44c8-b725-7fa06cb2d19f.png)

#### Caso seja necessário a alteração de uma env, simplismente será feita a alteração no catálogo e já teremos o nosso configmap atualizado para todos os serviços:
##### Exemplo, temos um erro na env DJONGA_ENV, nela temos o valor "sensassão"
![Captura de tela de 2022-06-04 23-24-28](https://user-images.githubusercontent.com/85401149/172032300-bfe0adc4-e259-4f45-b067-a16d23e818ec.png)
##### Vamos corrigir o valor no catálogo:
![Captura de tela de 2022-06-04 23-25-56](https://user-images.githubusercontent.com/85401149/172032326-b863a885-d0ec-4f24-b87b-fc697200762d.png)

