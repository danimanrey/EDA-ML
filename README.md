# EDA-ML (Exploratory Data Analysis with Machine Learning)

## Descripción

Este proyecto se centra en realizar un análisis exploratorio de datos (EDA) y construir modelos de regresión lineal para predecir el precio de ciertas criptomonedas en función de su capitalización de mercado. Se explorarán correlaciones influyentes, como la dominancia en el mercado y el volumen.

## Contenido del Repositorio

1. **data**: se almacenan los datos utilizados en el proyecto.
   - `raw`: Contiene los datos en su formato original, sin procesar.
   - `processed`: Almacena los datos procesados después de realizar las transformaciones necesarias antes de utilizarlos para el modelo.
   - `train`: Contiene los datos de entrenamiento utilizados para entrenar el modelo a partir de los datos procesados
   - `test`: Almacena los datos de prueba utilizados para evaluar el modelo a partir de los datos procesados

2. **notebooks**: se encuentran los archivos Jupyter Notebook que contienen el desarrollo del proyecto.
   - `01_Fuentes.ipynb`: adquisición de datos y unión de las diferentes fuentes.
   - `02_LimpiezaEDA.ipynb`: transformaciones y limpiezas, incluyendo el feature engineering, así como visualizaciones dentro de un análisis exploratiorio.
   - `03_Entrenamiento_Evaluacion.ipynb`: entrenamiento de modelos (mínimo 5 modelos supervisados diferentes y al menos 1 no supervisado) junto con su hiperparametrización, así como evaluación de los modelos.
3. **src**: contiene los archivos fuente de Python que implementan las funcionalidades clave del proyecto.
   - `data_processing.py`: código para procesar los datos de la carpeta `data/raw` y guardar los datos procesados en la carpeta `data/processed`.
   - `training.py`: código para entrenar y guardar el modelo entrenado con el input de los datos de la carpeta `data/processed` y guardar los datasets de `data/train` y `data/test` utilizados en el entrenamiento.
   - `evaluation.py`: código para evaluar el modelo utilizando los datos de prueba de la carpeta `data/test` y generar métricas de evaluación.

4. **models**: se almacenarán los archivos relacionados con el modelo entrenado:
   - `trained_model_n.pkl`: modelos entrenados y guardados en formato pickle, siendo n un identificador para cada modelo.
   - `final_model.pkl`: modelo final guardado en formato pickle.
   - `model_config.yaml`: archivo con la configuración del modelo final (parámetros)

5. **app**: contendrá los archivos necesarios para el despliegue del modelo en Streamlit u otra plataforma similar. Los requisitos son los siguientes:

   - `app.py`: código para la aplicación web que utiliza el modelo entrenado final(Streamlit).
   - `requirements.txt`: especifica las dependencias del proyecto para poder ejecutar la aplicación.

5. **docs**: contiene la documentación adicional relacionada con el proyecto, como presentaciones.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores, mejoras o deseas agregar más funcionalidades, no dudes en abrir un issue o enviar un pull request.

