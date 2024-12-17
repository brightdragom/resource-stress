FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu18.04

RUN echo 'export PATH=/usr/local/cuda-11.2bin${PATH:+:${PATH}}' >> ~/.bashrc
RUN echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
RUN echo 'export PATH=/usr/local/cuda/bin:/$PATH' >> ~/.bashrc
RUN echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
#RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until
# RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://kr.archive.ubuntu.com/ubuntu/|g' /etc/apt/sources.list

RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|https://mirror.kakao.com/ubuntu/|g' /etc/apt/sources.list
# RUN sed -i 's|http|https|g' /etc/apt/sources.list


RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev build-essential python-numpy python3-numpy
RUN apt-get install -y stressapptest stress-ng
# RUN apt-get install -y nvidia-cuda-toolkit
COPY ./ /app
COPY requirements.txt /app
WORKDIR /app

RUN pip3 install -r requirements.txt

# ENTRYPOINT ["python3"]
# CMD ["main.py"]

ENTRYPOINT ["python3"]
CMD ["app.py"]
