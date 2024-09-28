from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4
from pathlib import Path
import subprocess
import os

app = FastAPI(
    title="Lower Thirds Video API",
    description="An API to generate lower-thirds videos with user-provided details, such as full name, job title, and company name, and download the resulting `.mov` file.",
    version="1.0.0"
)

MOV_DIR = "mov_files"
os.makedirs(MOV_DIR, exist_ok=True)  # Ensure the output directory exists

MLT_TEMPLATE_PATH = "lower-thirds.mlt"

class LowerThirdsRequest(BaseModel):
    full_name: str = Field(..., title="Full Name", description="The full name of the person to appear in the lower-thirds.")
    job_title: str = Field(..., title="Job Title", description="The job title of the person to appear in the lower-thirds.")
    company_name: str = Field(..., title="Company Name", description="The name of the company to appear in the lower-thirds.")
    filename: Optional[str] = Field(None, title="Filename", description="The name of the output .mov file. If not provided, a default filename will be generated.")

    class Config:
        schema_extra = {
            "example": {
                "full_name": "John Doe",
                "job_title": "Senior Developer",
                "company_name": "Tech Corp"
            }
        }

def generate_mov_file(request: LowerThirdsRequest):
    try:
        # Generate a default filename if not provided
        if not request.filename:
            request.filename = f"{request.full_name.replace(' ', '_')}_{uuid4().hex}.mov"
        
        output_path = Path(MOV_DIR) / request.filename

        # Read and modify the MLT XML file to replace placeholders with actual data
        with open(MLT_TEMPLATE_PATH, 'r') as file:
            mlt_content = file.read()

        # Replace the placeholders with the values from the request
        mlt_content = mlt_content.replace("Firstname Lastname", request.full_name)
        mlt_content = mlt_content.replace("Job Title", request.job_title)
        mlt_content = mlt_content.replace("Company", request.company_name)

        # Save the modified MLT file to a temporary location
        temp_mlt_path = Path(MOV_DIR) / f"{uuid4().hex}.mlt"
        with open(temp_mlt_path, 'w') as file:
            file.write(mlt_content)

        # Command to create mov file using melt
        command = [
            "melt", "-progress2", "-abort", f"xml:{temp_mlt_path}", 
            "-consumer", f"avformat:{output_path}", "vcodec=qtrle", "pix_fmt=argb", "an=1"
        ]
        subprocess.run(command, check=True)

        # Clean up the temporary MLT file
        temp_mlt_path.unlink()

        return output_path
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error creating mov file: {e}")

@app.post("/lower-thirds/", 
          summary="Create and Download Lower Thirds Video", 
          description="Generates a lower-thirds `.mov` video based on the provided full name, job title, and company name. Once the video is generated, it will be available for download.",
          response_description="The generated .mov file will be returned for download.")
def create_and_download(request: LowerThirdsRequest):
    # Generate the mov file (this may take time)
    output_path = generate_mov_file(request)
    
    # Once done, return the file as a downloadable response
    if output_path.exists():
        return FileResponse(path=str(output_path), filename=request.filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
