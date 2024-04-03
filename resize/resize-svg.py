import os
import svgutils.transform as sg

print("******************************")

# if __name__ == "__main__":
logos = os.listdir("./logos")
for file in logos:
    print("Resizing ", file)
    path = os.path.join("./logos", file)
    fig = sg.fromfile(path)
    fig.set_size(("100", "100"))
    fig.save(path)
