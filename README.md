# lower-thirds

```bash
melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=qtrle pix_fmt=argb an=1
```

```bash
melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=prores_ks pix_fmt=yuva444p10le an=1
```

```bash
curl -X POST "http://localhost:8000/lower-thirds/" \
    -H "Content-Type: application/json" \
    -d '{
        "full_name": "John Doe", 
        "job_title": "Senior Developer", 
        "company_name": "Tech Corp"
    }' \
    --output generated_file.mov
```

```bash
docker run --rm -v $(pwd):/mnt mltframework/melt:latest -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=prores_ks pix_fmt=yuva444p10le an=1
```
