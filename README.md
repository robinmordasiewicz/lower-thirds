# lower-thirds

```bash
melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=qtrle pix_fmt=argb an=1
```

```bash
melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=prores_ks pix_fmt=yuva444p10le an=1
```

```bash
melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=prores_ks vprofile=4 vendor=apl0 movflags=+write_colr mlt_image_format=rgb pix_fmt=yuv444p10le
melt -progress2 -abort xml:lower-thirds.mlt -verbose -consumer avformat:outputqt.mov vcodec=prores_ks pix_fmt=yuva444p10le an=1
```

```bash
curl -X POST "http://localhost/lower-thirds/" \
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

```bash
docker run -d --name lower-thirds -p 80:8000 lower-thirds:latest
```

## Mac install dependencies

```bash
brew install cmake automake autoconf libtool pkg-config aribb24 chromaprint fdk-aac frei0r game-music-emu hwloc jack jpeg-xl libaribcaption libavif libbluray libbs2b libcaca libdv libdvdnav libdvdread libexif libgsm libmodplug libopenmpt libplacebo libquicktime librist librsvg libsoxr libssh libvmaf libxml2 opencore-amr openh264 openjpeg openssl openvino rav1e rtmpdump rubberband sdl2 sdl2_image speex srt svt-av1 tesseract two-lame vid.stab webp xvid zeromq zimg
```

```bash
brew reinstall homebrew-ffmpeg/ffmpeg/ffmpeg \
  --with-chromaprint \
  --with-dvd \
  --with-fdk-aac \
  --with-game-music-emu \
  --with-jack \
  --with-jpeg-xl \
  --with-libaribb24 \
  --with-libaribcaption \
  --with-libmodplug \
  --with-libopenmpt \
  --with-libplacebo \
  --with-librist \
  --with-librsvg \
  --with-libsoxr \
  --with-libssh \
  --with-tesseract \
  --with-libvidstab \
  --with-opencore-amr \
  --with-openh264 \
  --with-openjpeg \
  --with-openssl \
  --with-rav1e \
  --with-svt-av1 \
  --with-rtmpdump \
  --with-rubberband \
  --with-two-lame \
  --with-webp \
  --with-xvid \
  --with-zeromq \
  --with-zimg \
  --with-srt \
  --with-libvmaf \
  --with-libxml2 \
  --with-aribb24 \
  --with-libbluray \
  --with-libbs2b \
  --with-libcaca \
  --with-libdvdnav \
  --with-libdvdread \
  --with-libgsm \
  --with-speex
```

```bash
export CFLAGS="-I/opt/homebrew/include"
export LDFLAGS="-L/opt/homebrew/lib"
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig"
git clone https://github.com/mltframework/mlt.git
cd mlt
./configure --enable-gpl --enable-libx264 --enable-libx265 --enable-nonfree
make
sudo make install
```
