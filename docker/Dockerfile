# Dockerfile
FROM readthedocs/build:latest

# Install TeXworks for graphical LaTeX editing
RUN apt-get install -y texworks x11-apps && \
    apt-get clean

# Set environment variables for X11 forwarding
ENV DISPLAY=:99