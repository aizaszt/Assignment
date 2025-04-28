import random
from shapes import Sphere, Cylinder, Cube


def main():
    shapes = []

    for _ in range(10):
        shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])

        if shape_type == 'Sphere':
            radius = random.randint(1, 10)
            shape = Sphere(radius)
        elif shape_type == 'Cylinder':
            radius = random.randint(1, 10)
            height = random.randint(5, 20)
            shape = Cylinder(radius, height)
        else:  # Cube
            side_length = random.randint(1, 10)
            shape = Cube(side_length)

        shapes.append(shape)

    for idx, shape in enumerate(shapes, 1):
        print(f"Shape {idx}: {type(shape).__name__}")
        print(f"Surface Area: {shape.surface_area():.2f}")
        print(f"Volume: {shape.volume():.2f}")
        print('-' * 30)
$

if __name__ == "__main__":
    main()