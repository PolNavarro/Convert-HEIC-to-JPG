import os
import asyncio
from PIL import Image
import pillow_heif

async def convertir_imagen(ruta_archivo_HEIC, ruta_archivo_JPG):


    heif_file = pillow_heif.read_heif(ruta_archivo_HEIC)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    image.save(os.path.splitext(ruta_archivo_JPG)[0] + ".jpg", "JPEG")
    os.remove(ruta_archivo_HEIC)

async def revisar_carpeta(RUTA_CARPETA_HEIC, RUTA_CARPETA_JPG) :
    while True:
        for archivo in os.listdir(RUTA_CARPETA_HEIC):
            if archivo.endswith(".HEIC") or archivo.endswith(".heic"):

                ruta_archivo_HEIC = os.path.join(RUTA_CARPETA_HEIC, archivo)
                ruta_archivo_JPG = os.path.join(RUTA_CARPETA_JPG, archivo)
                asyncio.create_task(convertir_imagen(ruta_archivo_HEIC, ruta_archivo_JPG))
                
        # segundos k se revisa la carpeta
        await asyncio.sleep(60)

async def main():
    RUTA_CARPETA_HEIC = "./fotos"
    RUTA_CARPETA_JPG = "./fotospasadas"

    # Crea una tare para revisar la carpeta.
    asyncio.create_task(revisar_carpeta(RUTA_CARPETA_HEIC, RUTA_CARPETA_JPG))

    #Ejecuta el programo indefinidamente
    while True:
        await asyncio.sleep(1)

# Inciar programa
if __name__ == "__main__":
    asyncio.run(main())