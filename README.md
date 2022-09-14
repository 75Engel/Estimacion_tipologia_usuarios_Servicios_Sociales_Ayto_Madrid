# Estudio sobre la posibilidad de establecer algún método de Machine Learning en la previsión de acciones del área de Servicios Sociales del Ayto. Madrid para mejorar la atención al usuario de __urgencias__.

### Introducción:

Usando como base la información recabada y no utilizada en mi anterior estudio referente al área de Servicios Sociales del Ayto. de Madrid, vamos a valorar la viabilidad de determinar los procesos de atención de urgencias en el Ayto. de Madrid y la tipología de los usuarios que los demandan.

En el Ayto. de Madrid se consideran 5 posibles mótivos de urgencia. Estos son:

  >Malos tratos
  >
  >Abandono  
  >
  >Alojamiento/Vivienda
  >
  >Desprotección social problema salud  
  >
  >Desprotección socio-familiar 


---

### Qué pretendemos obtener: 

Con este estudio queremos ver si es posible __establecer una relación__ entre los casos que se suceden y diferentes variables y poder __realizar una previsión__ de cada tipo de urgencia que se atiende para periodos venideros.

Dada el limitado espacio de tiempo de los Datasets que se tienen, vamos a realizar un __estudio exploratorio de los datos__ en relación con la variable __tiempo__, que es una de las diferentes variables predictoras que podemos considerar en este proceso. 

Otras variables que planteamos como variables independientes serían __distrito, sexo, nacionalidad y el rango de la edad__ de los usuarios que realizan la gestión de la urgencia.

La __variable dependiente u objetivo__ sería la tipología del caso.


***

### Qué vamos a realizar: 

Primeramente vamos a realizar un __Análisis Exploratorio de datos__  para valorar cómo se commportan las posibles variables predictoras.

Segundo realizaremos procesos de __ingeniería de datos__ para poder utilizar la información recabada y **realizar modelados**.

Tercero, realizaremos modelados conjuntamente con ingeniería de datos para optimizar los primeros, midiendo **métricas** que permitan valorar una **variable objetivo multiclase**.


Finalmente, procederemos a establecer la **importancia de las variables predictoras** en el módelo escogido.


***

### Datos utilizados:
Los datos obtenidos han sido a través de un Dataset publicado en el __portal de Datos Abiertos del Ayuntamiento de Madrid__ desde  el año  2018 hasta el 2021.

Este último año no está completo a pesar que se debería de actualizar trimestralmente la información presentada en este portal. Los datos que se disponen son únicamente hasta el mes de julio.
  >[Urgencias atendidas desde los Servicios Sociales del Ayuntamiento de Madrid][Data_1]

  >[Estructura del conjunto de datos][Data_2]



[Data_1]:https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=0b006dace9578610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default
[Data_2]:https://datos.madrid.es/FWProjects/egob/Catalogo/SociedadBienestar/Ficheros/Estructura_DS_Urgencias_Centros_Servicios_Sociales.pdf



