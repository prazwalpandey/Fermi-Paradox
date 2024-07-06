import tkinter as tk
from random import randint, uniform, random
import math

SCALE = 225

num_civilizations = 15600000

root = tk.Tk()
root.title("Milky Way Galaxy")
c = tk.Canvas(root, width=1000, height=800, bg="black")
c.grid()
c.configure(scrollregion=(-500, -400, 500, 400))

disc_radius = 50000
disc_height = 1000
disc_volume = math.pi * disc_radius**2 * disc_height


def scale_galaxy():
    disc_radius_scaled = round(disc_radius / SCALE)
    bubble_volume_scaled = (4 / 3) * math.pi * (SCALE / 2) ** 3
    return disc_radius_scaled, bubble_volume_scaled


def detection_probability(disc_vol_scaled):
    ratio = num_civilizations / disc_vol_scaled
    if ratio < 0.02:
        detection_probability = 0
    elif ratio >= 5:
        detection_probability = 1
    else:
        detection_probability = (
            -0.004748 * ratio**4
            + 0.06666 * ratio**3
            - 0.3596 * ratio**2
            + 0.9191 * ratio**1
            + 0.01036
        )
    return round(detection_probability, 3)


def random_polar_coordinates(disc_radius_scaled):
    r = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * disc_radius_scaled)
    y = round(math.sqrt(r) * math.sin(theta) * disc_radius_scaled)
    return x, y


def spiral_arms(b, r, rot_fac, fuz_fac, arm):
    spiral_stars = []
    fuzz = int(0.030 * abs(r))
    theta_max_degree = 520
    for i in range(theta_max_degree):
        theta = math.radians(i)
        x = (
            r * math.cos(theta + math.pi * rot_fac) * math.exp(b * theta)
            + randint(-fuzz, fuzz) * fuz_fac
        )
        y = (
            r * math.sin(theta + math.pi * rot_fac) * math.exp(b * theta)
            + randint(-fuzz, fuzz) * fuz_fac
        )
        spiral_stars.append((x, y))

    for x, y in spiral_stars:
        if arm == 0 and int(x % 2) == 0:
            c.create_oval(x - 2, y - 2, x + 2, y + 2, fill="white", outline="")
        elif arm == 0 and int(x % 2) != 0:
            c.create_oval(x - 1, y - 1, x + 1, y + 1, fill="white", outline="")
        elif arm == 1:
            c.create_oval(x, y, x, y, fill="white", outline="")


def star_haze(disc_radius_scaled, density):
    for i in range(0, disc_radius_scaled * density):
        x, y = random_polar_coordinates(disc_radius_scaled)
        c.create_text(x, y, fill="white", font=("Helvetica", "7"), text=".")


def main():

    disc_radius_scaled, disc_volume_scaled = scale_galaxy()
    detection_prob = detection_probability(disc_volume_scaled)
    spiral_arms(b=-0.3, r=disc_radius_scaled, rot_fac=2, fuz_fac=1.5, arm=0)
    spiral_arms(b=-0.3, r=disc_radius_scaled, rot_fac=1.91, fuz_fac=1.5, arm=1)
    spiral_arms(b=-0.3, r=-disc_radius_scaled, rot_fac=2, fuz_fac=1.5, arm=0)
    spiral_arms(b=-0.3, r=-disc_radius_scaled, rot_fac=-2.09, fuz_fac=1.5, arm=1)
    spiral_arms(b=-0.3, r=-disc_radius_scaled, rot_fac=0.5, fuz_fac=1.5, arm=0)
    spiral_arms(b=-0.3, r=-disc_radius_scaled, rot_fac=0.4, fuz_fac=1.5, arm=1)
    spiral_arms(b=-0.3, r=-disc_radius_scaled, rot_fac=-0.5, fuz_fac=1.5, arm=0)
    spiral_arms(b=-0.3, r=-disc_radius_scaled, rot_fac=-0.6, fuz_fac=1.5, arm=1)
    star_haze(disc_radius_scaled, 8)

    c.create_text(
        -455, -360, fill="white", anchor="w", text="One Pixel = {} LY".format(SCALE)
    )
    c.create_text(
        -455,
        -330,
        fill="white",
        anchor="w",
        text="Radio Bubble Diameter = {} LY".format(SCALE),
    )
    c.create_text(
        -455,
        -300,
        fill="white",
        anchor="w",
        text="Probability of Detection for {:,} Civilizations= {}".format(
            num_civilizations, detection_prob
        ),
    )

    if SCALE == 225:
        c.create_rectangle(115, 75, 116, 76, fill="red", outline="")
        c.create_text(
            118,
            72,
            fill="red",
            anchor="w",
            text="<-----------------------------Earth's Radio Bubble",
        )

    root.mainloop()


if __name__ == "__main__":
    main()
