# CAMMESA API - Data Visualization

Proyecto tendiente a obtener datos de la [API Web de CAMMESA](https://microfe.cammesa.com/static-content/CammesaWeb/download-manager-files/Api/Documentacion%20API%20Web.pdf), su almacenamiento en MongoDB Atlas y posterior visualizaci贸n utilizando Streamlit.

Accede al **[Deployment](https://cammesa.herokuapp.com/)**.


## Deploy 馃摝

Algunas capturas del deploy.

![CAMMESA App Gif](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Streamlit_app.gif?raw=true)

![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_1.png?raw=true)
![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_2.png?raw=true)
![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_3.png?raw=true)
![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_4.png?raw=true)
![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_5.png?raw=true)
![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_6.png?raw=true)
![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_7.png?raw=true)
![CAMMESA App Screnshot 1](https://github.com/ValentinSilvestri/cammesa/blob/master/assets/Screenshot_8.png?raw=true)


## WIP 馃敡

Actualmente solo se han creado las p谩ginas de demanda por regi贸n (datos con una frecuencia de 5 min, actualizados al cargar la p谩gina), cuencas y perturbaciones del SADI (datos hist贸ricos hasta el 03/01/2022).

* Creaci贸n de las restantes p谩ginas.
* Actualizaci贸n on demand de los datos hist贸ricos almacenados en MongoDB.
* Incorporaci贸n de tooltips y widgets a los elementos gr谩ficos. Incorporaci贸n de gr谩ficos adicionales en las actuales p谩ginas.


## Construido con 馃洜锔?

Herramientas utilizadas:

* [MongoDB Atlas](https://www.mongodb.com/atlas) - Cloud NoSQL Database.
* [Streamlit](https://docs.streamlit.io/) - Open-source python app framework.
* [Heroku](https://www.heroku.com/) - Cloud platform as a service, used to deploy the Streamlit app.

Endpoints:
* [Demanda y Generac贸n de Energ铆a](https://api.cammesa.com/demanda-svc/swagger-ui.html) - Permite el acceso a la informaci贸n de Demanda y Generac贸n de Energ铆a disponibles para los Agentes de CAMMESA.
* [Publicaciones](https://api.cammesa.com/pub-svc/swagger-ui.html) - Permite el acceso a las publicaciones de documentos disponibles para los Agentes de CAMMESA.


## Contribuyendo 馃枃锔?

Cualquier tipo de contribuci贸n es bienvenida, tales como [Bugs](https://github.com/ValentinSilvestri/cammesa/issues), [Pull requests](https://github.com/ValentinSilvestri/cammesa/pulls) y comentarios.


## Licencia 馃搫

Este proyecto est谩 bajo la _MIT License_ - mira el archivo [LICENSE](LICENSE) para detalles.

---
鈱笍 con 鉂わ笍 y 鈽? por [VSilvestri](https://www.linkedin.com/in/valentinsilvestri/).