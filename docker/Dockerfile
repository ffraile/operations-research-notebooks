# Dockerfile
FROM ubuntu:20.04

# Install necessary tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip make latexmk && \
    apt-get install -y texlive-full texstudio && \
    apt-get clean && rm -rf /var/lib/apt/lists/*



# Install Sphinx and any other necessary Python dependencies
RUN pip3 install sphinx readthedocs-sphinx-ext

# Since mounted volume files are not available in run time, we copy the requirements files here
COPY ../docs/requirements.txt .

RUN pip3 install requirements.txt

# Set the working directory
WORKDIR /docs

# Default command (we'll override this in Docker Compose for each service)
CMD ["bash"]
