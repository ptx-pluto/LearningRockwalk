import pybullet as p
import rock_walk.resources
import os

if __name__ == "__main__":
    p.connect(p.DIRECT)
    dir_name = os.path.join(
        os.path.dirname(__file__),
        'rock_walk',
        'resources',
        'models',
        'mesh'
    )
    name_in = os.path.join(dir_name, 'half_cy.obj')
    name_out = os.path.join(dir_name, 'half_cy_hvacd.obj')
    name_log = "log.txt"
    p.vhacd(name_in, name_out, name_log)
