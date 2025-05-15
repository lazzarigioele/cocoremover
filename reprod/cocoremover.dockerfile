FROM lazzarigioele/python39:latest

COPY cocoremover.yml /home/jovyan/
RUN \
conda config --system --prepend channels bioconda && \
mamba env update -n base --file /home/jovyan/cocoremover.yml && \
mamba clean --all -f -y && \
rm /home/jovyan/cocoremover.yml
