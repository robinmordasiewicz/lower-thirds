# lower-thirds

## Manual Rendering

### locally installed mlt framework

```bash
melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:lower-thirds.webm an=1 rc_lookahead=16 quality=good speed=3 vprofile=0 qmax=51 qmin=4 slices=4 tile-columns=6 frame-parallel=1 lag-in-frames=25 row-mt=1 auto-alt-ref=0 mlt_image_format=rgba pix_fmt=yuva420p an=1 vcodec=libvpx-vp9 crf=30
```

### docker run mltframework

```bash
docker run --rm -e SDL_AUDIODRIVER=dummy -e AUDIODEV=null -v $(pwd):/mnt mltframework/melt:latest -progress2 -abort xml:lower-thirds.mlt -consumer avformat:lower-thirds.webm an=1 rc_lookahead=16 quality=good speed=3 vprofile=0 qmax=51 qmin=4 slices=4 tile-columns=6 frame-parallel=1 lag-in-frames=25 row-mt=1 auto-alt-ref=0 mlt_image_format=rgba pix_fmt=yuva420p an=1 vcodec=libvpx-vp9 crf=30
```

## API

### Run the container

```bash
docker run -d --name lower-thirds -p 80:8000 lower-thirds:latest
```

### API request

```bash
curl -X POST "http://localhost/video/lower-thirds/" \
    -H "Content-Type: application/json" \
    -d '{
        "full_name": "John Doe",
        "job_title": "Senior Developer", 
        "company_name": "Tech Corp"
    }' \
    --output lower-thirds.webm
```

## Mac install

```bash
brew install cmake automake autoconf libtool pkg-config aribb24 chromaprint fdk-aac frei0r game-music-emu hwloc jack jpeg-xl libaribcaption libavif libbluray libbs2b libcaca libdv libdvdnav libdvdread libexif libgsm libmodplug libopenmpt libplacebo libquicktime librist librsvg libsoxr libssh libvmaf libxml2 opencore-amr openh264 openjpeg openssl openvino rav1e rtmpdump rubberband sdl2 sdl2_image speex srt svt-av1 tesseract two-lame vid.stab webp xvid zeromq zimg tesseract-lang qt@5 swig fftw pmix open-mpi libebur128 clang-format gdk-pixbuf openal-soft glew
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
xcode-select --install
softwareupdate --list
softwareupdate --install --all
export CFLAGS="-I/opt/homebrew/include"
export LDFLAGS="-L/opt/homebrew/lib"
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig"
export CMAKE_PREFIX_PATH="/opt/homebrew/opt/qt@5:$CMAKE_PREFIX_PATH"
git clone https://github.com/mltframework/mlt.git
cd mlt
cmake -DMovit=OFF -DRtAudio=OFF -DSpatialAudio=OFF -DLADSPA=OFF -DWITH_ALL_PLUGINS=ON -DMLT_INSTALL_PLUGINS_DIR=/usr/local/PlugIns/mlt .
cmake --build .
sudo cmake --install .
```
