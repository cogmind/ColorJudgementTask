'''
Created on May 19, 2016

@author: Daniel Labbe
'''


from math import pi

class ColorWheel(object):

        self.CX = 0
        self.CY = 0
        self.R  = None
        self.xs = []
        self.ys = []

    def __init__(self, R, CX, CY):
        self.R = R
        self.CX = CX
        self.CY = CY

        #circle width w
        #triangle height h
        #triangle base b
        inner_radius = R - w
        outer_radius = R + w
        h = w
        inner_circ = 2 * pi * inner_radius
        outer_circ = 2 * pi * outer_radius
        b = outer_circ / inner_circ
        #area = b * h / 2
        triangles = inner_circ
        delta_angle = 360 / triangles

        #For
        prep_circle(inner_radius)
        prep_circle(outer_radius)

    def prep_circle(self, R):
        # The Fast Bresenham Algorithm (Kennedy-Bresenham)
        # Based on John Kennedy, 2001
        # http://web.engr.oregonstate.edu/~sllu/bcircle.pdf
        x = R
        y = 0
        x_change = 1 - 2 * R
        y_change = 1
        radius_error = 0
        while (x >= y):
            xs, ys = plot_symmetric_points(x, y)
            #Potential memory overhead. Consider revising
            self.xs.append(xs)
            self.ys.append(ys)
            y += 1
            radius_error = radius_error + y_change
            ychange = ychange + 2
            if (2 * radius_error + x_change) > 0:
                x = x - 1
                radius_error = radius_error + x_change
                x_change = x_change + 2


    def plot_symmetric_points(x, y):
        x_offset = [x, -x, -x, x, y, -y, -y, y]
        y_offset = [y, y, -y, -y, x, x, -x, -x]
        xs = [x_ + self.XC for x_ in x_offset]
        ys = [y_ + self.YC for y_ in y_offset]

        return xs, ys


    def draw_circle(self, x, y):
        pass


class Brush(object):
    '''
    classdocs
    '''


    def __init__(self, x_start, y_start):
        '''
        The Murphy-Bresenham Algorithm

        Murphy, A. A. (1978). IBM Technical Disclosure Bulletin, 20(12), 5358-5366. http://homepages.enterprise.net/murphy/thickline/
        Copyright A S Murphy 1999

        Modified by Daniel Labbe (2016)
        '''

        x_end = None
        x_start = None
        y_start = None
        y_end = None

        u = x_end - x_start;
        v = None
        p = 0
        d = 0
        k = u^2 + v^2
        ku = 2 * u

        # Square shift change
        kv = 2 * v
        # Diagional shift change
        kd = kv - ku

        # Diagional/Square decision treshold
        kt = u - kv

        ks = kv + ku
        ki = 2 * k

        m0 = None
        m1 = None
        m2 = None
        m3 = None
        par = self.parityOf(0)
        do = 0
        di = 0


    def parityOf(self, int_type):
        #https://wiki.python.org/moin/BitManipulation
        parity = 0
        while (int_type):
            parity = ~parity
            int_type = int_type & (int_type - 1)
            return(parity)

