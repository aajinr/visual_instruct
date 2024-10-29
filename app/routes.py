from fastapi import APIRouter, File, UploadFile,HTTPException
from fastapi.responses import JSONResponse
from io import BytesIO
from PIL import Image
import numpy as np

from llama_predict import predict
router=APIRouter()

@router.post("/predict/")
async def describe_image(file: UploadFile= File(...))
    try:
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG images are supported")
        
        image_data=await file.read()
        image=Image.open(BytesIO(image_data)).convert("RGB") #convert to rgb for consistency

        #run description prediction
        prediction=predict(image)
        return prediction
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Description error: {str(e)}")