from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4
from pathlib import Path
import subprocess
import os

# FastAPI app with video API paths
app = FastAPI(
    title="Lower Thirds and Eyebrow Video API",
    description="APIs to generate videos such as lower-thirds and eyebrow with user-provided details and download the resulting `.mov` files.",
    version="1.1.0",
    docs_url="/video/docs/",
    redoc_url="/video/redocs/",
    openapi_url="/video/openapi.json"
)

MOV_DIR = "assets"
os.makedirs(MOV_DIR, exist_ok=True)  # Ensure the output directory exists

MLT_LOWER_THIRDS_TEMPLATE_PATH = "lower-thirds.mlt"
MLT_EYEBROW_TEMPLATE_PATH = "eyebrow.mlt"

class LowerThirdsRequest(BaseModel):
    full_name: str = Field(..., title="Full Name", description="The full name of the person to appear in the lower-thirds.")
    job_title: str = Field(..., title="Job Title", description="The job title of the person to appear in the lower-thirds.")
    company_name: str = Field(..., title="Company Name", description="The name of the company to appear in the lower-thirds.")
    filename: Optional[str] = Field(None, title="Filename", description="The name of the output .mov file. If not provided, a default filename will be generated.")

class EyebrowRequest(BaseModel):
    title_one: str = Field(..., title="Title One", description="The first title to appear in the eyebrow video.")
    title_two: str = Field(..., title="Title Two", description="The second title to appear in the eyebrow video.")
    filename: Optional[str] = Field(None, title="Filename", description="The name of the output .mov file. If not provided, a default filename will be generated.")

def generate_mov_file(template_path: str, replacements: dict, output_filename: str):
    try:
        output_path = Path(MOV_DIR) / output_filename

        # Read and modify the MLT XML file to replace placeholders with actual data
        with open(template_path, 'r') as file:
            mlt_content = file.read()

        # Replace the placeholders in the template with the values from the replacements dictionary
        for placeholder, value in replacements.items():
            mlt_content = mlt_content.replace(placeholder, value)

        # Save the modified MLT file to a temporary location
        temp_mlt_path = Path(MOV_DIR) / f"{uuid4().hex}.mlt"
        with open(temp_mlt_path, 'w') as file:
            file.write(mlt_content)

        # Command to create mov file using melt
        command = [
            "xvfb-run", "-a", "melt", "-progress2", "-abort", f"xml:{temp_mlt_path}", 
            "-consumer", f"avformat:{output_path}", "an=1", "rc_lookahead=16", "quality=good", "speed=3", "vprofile=0", "qmax=51", "qmin=4", "slices=4", "tile-columns=6", "frame-parallel=1", "lag-in-frames=25", "row-mt=1", "auto-alt-ref=0", "mlt_image_format=rgba", "pix_fmt=yuva420p an=1", "vcodec=libvpx-vp9", "crf=30"
        ]
        subprocess.run(command, check=True)

        # Clean up the temporary MLT file
        temp_mlt_path.unlink()

        return output_path
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error creating mov file: {e}")

@app.post("/video/lower-thirds/", 
          summary="Create and Download Lower Thirds Video", 
          description="Generates a lower-thirds `.webm` video based on the provided full name, job title, and company name. Once the video is generated, it will be available for download.",
          response_description="The generated .webm file will be returned for download.")
def create_and_download_lower_thirds(request: LowerThirdsRequest):
    # Generate a default filename if not provided
    if not request.filename:
        request.filename = f"{request.full_name.replace(' ', '_')}_{uuid4().hex}.webm"
    
    # Generate the mov file for lower thirds
    replacements = {
        "Firstname Lastname": request.full_name,
        "Job Title": request.job_title,
        "Company": request.company_name
    }
    output_path = generate_mov_file(MLT_LOWER_THIRDS_TEMPLATE_PATH, replacements, request.filename)
    
    # Return the file as a downloadable response
    if output_path.exists():
        return FileResponse(path=str(output_path), filename=request.filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.post("/video/eyebrow/", 
          summary="Create and Download Eyebrow Video", 
          description="Generates an eyebrow `.webm` video based on the provided titles. Once the video is generated, it will be available for download.",
          response_description="The generated .webm file will be returned for download.")
def create_and_download_eyebrow(request: EyebrowRequest):
    # Generate a default filename if not provided
    if not request.filename:
        request.filename = f"eyebrow_{uuid4().hex}.webm"
    
    # Generate the mov file for eyebrow
    replacements = {
        "VAR_TITLE_ONE": request.title_one,
        "VAR_TITLE_TWO": request.title_two
    }
    output_path = generate_mov_file(MLT_EYEBROW_TEMPLATE_PATH, replacements, request.filename)
    
    # Return the file as a downloadable response
    if output_path.exists():
        return FileResponse(path=str(output_path), filename=request.filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/video/health/", 
         summary="Health Check", 
         description="Health check endpoint to verify the API is running correctly.")
def health_check():
    return JSONResponse(status_code=200, content={"status": "200 OK"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
