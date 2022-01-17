# CAMMESA API - Data Visualization

Proyecto tendiente a obtener datos de la [API Web de CAMMESA](https://microfe.cammesa.com/static-content/CammesaWeb/download-manager-files/Api/Documentacion%20API%20Web.pdf), su almacenamiento en MongoDB Atlas y posterior visualización utilizando Streamlit.

Accede al **[Deployment](https://cammesa.herokuapp.com/)**.


## Deploy 📦

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


## WIP 🔧

Actualmente solo se han creado las páginas de demanda por región (datos con una frecuencia de 5 min, actualizados al cargar la página), cuencas y perturbaciones del SADI (datos históricos hasta el 03/01/2022).

* Creación de las restantes páginas.
* Actualización on demand de los datos históricos almacenados en MongoDB.
* Incorporación de tooltips y widgets a los elementos gráficos. Incorporación de gráficos adicionales en las actuales páginas.


## Construido con 🛠️

Herramientas utilizadas:

* [MongoDB Atlas](https://www.mongodb.com/atlas) - Cloud NoSQL Database.
* [Streamlit](https://docs.streamlit.io/) - Open-source python app framework.
* [Heroku](https://www.heroku.com/) - Cloud platform as a service, used to deploy the Streamlit app.

Endpoints:
* [Demanda y Generacón de Energía](https://api.cammesa.com/demanda-svc/swagger-ui.html) - Permite el acceso a la información de Demanda y Generacón de Energía disponibles para los Agentes de CAMMESA.
* [Publicaciones](https://api.cammesa.com/pub-svc/swagger-ui.html) - Permite el acceso a las publicaciones de documentos disponibles para los Agentes de CAMMESA.


## Contribuyendo 🖇️

Cualquier tipo de contribución es bienvenida, tales como [Bugs](https://github.com/ValentinSilvestri/cammesa/issues), [Pull requests](https://github.com/ValentinSilvestri/cammesa/pulls) y comentarios.


## Licencia 📄

Este proyecto está bajo la _MIT License_ - mira el archivo [LICENSE](LICENSE) para detalles.

---
⌨️ con ❤️ y ☕ por [VSilvestri](https://www.linkedin.com/in/valentinsilvestri/).