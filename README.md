# Estudio sobre la posibilidad de establecer algún método de Machine Learning en la previsión de acciones del área de Servicios Sociales del Ayto. Madrid para mejorar la atención al usuario de __urgencias__.

### Introducción:

Usando como base la información recabada y no utilizada en mi anterior estudio referente al área de Servicios Sociales del Ayto. de Madrid, vamos a valorar la viabilidad de determinar los procesos de atención de urgencias en el Ayto. de Madrid y la tipología de los usuarios que los demandan.

En el Ayto. de Madrid se consideran 5 posibles mótivos de urgencia. Estos son:

  >Malos tratos       
  >Abandono  
  >Alojamiento/Vivienda
  >Desprotección social problema salud  
  >Desprotección socio-familiar 


---

### Qué pretendemos obtener: 

Con este estudio queremos ver si es posible establecer una relación entre los casos que se suceden y poder hacer una previsión de cada tipo de urgencia que se atiende en periodos venideros, así como observar si hay algún tipo de relación con las diferentes variables demográficas y la tipología de estas urgencias.

Dada el limitado espacio de tiempo de los Datasets que se tienen, vamos a realizar un estudio trimestral de los datos para tener más valores de las variables tiempo.

La variable tiempo es una de las diferentes variables que se consideran en este proceso. Otras variables que planteamos como variables independientes serían distrito, sexo, nacionalidad y el rango de la edad de los usuarios que realizan la gestión de la urgencia.

La variable dependiente u objetivo sería la tipología del caso.


***

### Datos utilizados:
Los datos obtenidos han sido a través de diferentes Datasets publicados en el __portal de Datos Abiertos del Ayuntamiento de Madrid__ desde  el año  2018 hasta el 2021.

Este último año no está completo a pesar que se debería de actualizar trimestralmente la información presentada en este portal. Los datos que se disponen son únicamente hasta el mes de julio.
  >[Urgencias atendidas desde los Servicios Sociales del Ayuntamiento de Madrid][Data_1]

  >[Estructura del conjunto de datos][Data_2]



[Data_1]:https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=0b006dace9578610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default
[Data_2]:https://datos.madrid.es/FWProjects/egob/Catalogo/SociedadBienestar/Ficheros/Estructura_DS_Urgencias_Centros_Servicios_Sociales.pdf



