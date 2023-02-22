# Convert-HEIC-to-JPG

He creado un programa asíncrono para convertir automáticamente fotos.

Las siguientes dos variables son importantes:

El valor de la variable se refiere a la carpeta donde se encuentran las fotos.


```python
    RUTA_CARPETA_HEIC = "./fotos"
    RUTA_CARPETA_JPG = "./fotos_convertidas"
```

La carpeta "Heic" es donde se encuentran las fotos Heic, y la carpeta "JPG" es donde se guardarán las fotos una vez que se haya realizado la conversión.

Puedes ajustar el intervalo de tiempo en segundos para revisar la carpeta con el siguiente código:

```python
    # segundos k se revisa la carpeta
    await asyncio.sleep(60)
```
