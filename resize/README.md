# Python container and resize script

It is used to resize all the svg files in the logos folder to be consistent.

It uses the [svgutils library](https://svgutils.readthedocs.io/).

For the dockerfile, I simply put python as an ENTRYPOINT and run the script
with:

```bash
docker built -t pythoncontainer .
docker run  \
    -v $(dirname $(pwd))/logos:/app/logos \
    -v $(pwd)/resize-svg.py:/app/resize-svg.py \
    pythoncontainer
```

Happy coding
