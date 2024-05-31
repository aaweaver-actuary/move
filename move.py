from typing import Tuple

import numpy as np
import pyautogui as g
from scipy.stats import norm
from tqdm import tqdm

try:
    teams_bar = g.locateOnScreen(r"C:\Users\aweaver\move\teams-topbar.png")
except:
    try:
        teams_bar = g.locateOnScreen(r"C:\Users\aweaver\move\teams-topbar2.png")
    except:
        try:
            teams_bar = g.locateOnScreen(r"C:\Users\aweaver\move\teams-topbar3.png")
        except:
            # just in case the image is not found, go to the center of the screen, slightly
            # offset from the top
            teams_bar = (g.size()[0] / 2, 50, 100, 100)


def one_iter(duration: float, movement: Tuple[int, int], movement_dir: float):
    for _ in tqdm(range(int(duration)), desc=f"Waiting to move {movement}"):
        g.sleep(1)
    xdir = int(np.exp(norm.rvs(0, 2)) * movement[0])
    ydir = int(np.exp(norm.rvs(0, 2)) * movement[1])

    def dur():
        rand_values = np.round(np.exp(norm.rvs(0, 1, size=9)) * movement_dir, 2)

        # return a generator:
        for i in rand_values:
            yield i

    # instance of generator:
    dur = dur()

    g.moveRel(xdir, ydir, duration=next(dur))
    g.moveRel(-xdir, -ydir, duration=next(dur))
    g.moveRel(xdir, 2 * ydir, duration=next(dur))
    g.moveRel(-xdir, -2 * ydir, duration=next(dur))
    g.moveRel(xdir, ydir, duration=next(dur))
    g.moveRel(-2 * xdir, -ydir, duration=next(dur))
    g.moveRel(2 * xdir, ydir, duration=next(dur))
    g.moveRel(-xdir, -ydir, duration=next(dur))
    g.moveRel(xdir, ydir, duration=next(dur))

    g.moveTo(teams_bar[0] + 150, teams_bar[1] + 150, duration=1)
    g.click()
    g.press("esc")
    g.press("esc")
    g.moveTo(g.size()[0] / 2, g.size()[1] / 2, duration=1)


def main():
    while True:
        nsec = 5.0
        one_iter(nsec, (10, 5), 1)
        one_iter(nsec, (5, 10), 1)
        one_iter(nsec, (-10, -5), 1)
        one_iter(nsec, (-5, -10), 1)

        g.moveTo(g.size()[0] / 2, g.size()[1] / 2, duration=1)

        # clear console
        print("\033c", end="")


if __name__ == "__main__":
    main()
