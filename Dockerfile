
FROM node:slim

WORKDIR /app

COPY . .

EXPOSE 5000

RUN apt-get update && \
	apt-get install -y ffmpeg bash python3 python3-pip && \
    apt-get install -y curl unzip wget net-tools && \
    chmod +x entry_point.sh
	
RUN python3 -m pip install yt_dlp --break-system-packages
RUN python3 -m pip install streamlit --break-system-packages  

ENTRYPOINT ["./entry_point.sh"]
