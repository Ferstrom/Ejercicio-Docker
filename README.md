# Ejercicio-Docker

# instalar web.py

pip install web.py 

# Visualizar lista de paquetes 

pip freeze 

# Instalar todos los paquetes necesarios

pip3 install -r requirements.txt

# Ejecutar la aplicacion web 

python3 app.py

# Hacer un requirements con las versiones que han sido instaladas

pip3 freeze > requirements.txt



------------------------------------------------------------------------------
# Generar una imagen en docker 
docker build -t luis:v1

# Iniciar sesion en docker
docker login

# 
docker tag image:tag luis:v1 username/prueba

# Ver las imagenes que hay
docker images

#
docker push ferstrom/prueba