FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
  sudo \
  wget \
  vim \
  gcc \
  mysql-server \
  libmysqlclient-dev \
  libsm6 \
  libxext6 \
  libxrender-dev
# 作業ディレクトリをoptに指定
WORKDIR /opt
# anacondaのインストーラを取得。インストール実行。インストーラ削除
RUN wget https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh && \
  sh Anaconda3-2019.10-Linux-x86_64.sh -b -p /opt/anaconda3 && \
  rm -f Anaconda3-2019.10-Linux-x86_64.sh
# anaconda3のbinにpathを通す
ENV PATH /opt/anaconda3/bin:$PATH
# requirements.txtを追加する
WORKDIR /mounted_folder
COPY requirements.txt ./
# pipをインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /mounted_folder/d_matchapp