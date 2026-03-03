# Propósito del Código
El propósito del presente código es diseñar e implementar un filtro digital con el objetivo de analizar y mejorar una señal contaminada por ruido. En el procesamiento digital de señales, es común que las señales reales contengan componentes no deseadas que afectan su calidad y dificultan la interpretación de la información útil. Por ello, el filtrado digital es una herramienta fundamental para eliminar o atenuar dichas perturbaciones.

En este caso, el código genera una señal compuesta por varias frecuencias sinusoidales y posteriormente le añade ruido blanco para simular un entorno real. A partir de esta señal de entrada, se diseña un filtro digital pasa-bajas tipo Butterworth, el cual permite conservar las componentes de baja frecuencia y reducir las de alta frecuencia.

El programa no solo implementa el filtro, sino que también realiza un análisis comparativo antes y después del proceso de filtrado. Para ello, se visualiza la señal en el dominio del tiempo y en el dominio de la frecuencia mediante la Transformada Rápida de Fourier (FFT). Esto permite observar de manera clara cómo el filtro modifica el contenido espectral de la señal.

En síntesis, el código tiene como finalidad demostrar el funcionamiento práctico de los filtros digitales, analizar su efecto sobre señales contaminadas y comprender la importancia del diseño adecuado de parámetros como la frecuencia de corte y el orden del filtro. Este procedimiento es esencial en aplicaciones de ingeniería como telecomunicaciones, procesamiento de audio, sistemas biomédicos y control automático.
