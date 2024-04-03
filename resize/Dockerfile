FROM python:slim

RUN pip install svgutils

WORKDIR /app
COPY ./resize-svg.py .

CMD \
    echo "pwd inside the dockerfile is $(pwd)" && \
    echo "The python binary is in $(which python)" && \
    echo "Python version: $(python --version)" && \
    echo "" && \
    python resize-svg.py

# ENTRYPOINT python
# CMD /app/resize-svg.py
