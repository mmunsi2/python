import numpy
from scipy.ndimage import label
import matplotlib.pyplot as plt
from timeit import time

timing_results = {}
def plot_timing(func):
    global timing_results
    def _wrapper(x, y, color, *args, **kwargs):
        time_before = time.time()
        func_call_result = func(x, y, color, *args, **kwargs)
        time_after = time.time()
        total_time_spend = time_after - time_before
        print "Total time spent: {0}".format(str(total_time_spend))
        print "Total array size: {0}\n".format(numpy.size(func_call_result.pixels))
        timing_results.update(func_call_result(numpy.size(func_call_result.pixels), total_time_spend))
        return func_call_result
    return _wrapper

class Canvas(object):
    def __init__(self, pixels):
        self.pixels = pixels

    def __str__(self):
        return '\n'.join(map(lambda row: ''.join(row), self.pixels))

    def fill(self, x, y, color):
        """
        Fills a region of color at a given location with a given color.

        :param x:  the x coordinate where the user clicked
        :param y: the y coordinate where the user clicked
        :param color: the specified color to change the region to
        """
        raise NotImplementedError  # Override this function in the Solution classes


class Solution1(Canvas):
    """
    Recursive flood fill algorithm (4 directions)
    This algorithm has drawback in python due to existance of maximum recursion depth restriction
    It's much better to use iteration algorithms instead of usage of recursion in python,
    but it's also possible manually set recursion limit with sys.setrecursionlimit 
    """
    _flood_fill_name = u"Recursive flood fill"
    def flood_fill(self, x, y, color):
        self.recursion_depth+=1
        if self.pixels[x][y] == self.pointer_pixel_color:
            self.pixels[x][y] = color
            #recursively go through all cells
            if x > 0:
                self.flood_fill(x-1,y, color)
            if x < len(self.pixels) - 1:
                self.flood_fill(x+1,y, color)
            if y > 0:
                self.flood_fill(x,y-1, color)
            if y < len(self.pixels[x]) - 1:
                self.flood_fill(x,y+1, color)
    
    @plot_timing
    def fill(self, x, y, color):
        self.recursion_depth=0
        self.pointer_pixel_color = self.pixels[x][y]
        try:
            self.flood_fill(x, y, color)
        except Exception as e:
            print(e)
        return self
        


class Solution2(Canvas):
    """
    Flood fill algorithm (4 directions) with a stack approach. Such approach is more appropriate than the usage of recursion in Solution1
    because it won't generate too deep recursion exception in python
    The most effective methods are based on stack or queue with a usage of loop with "eastern" or "western" direction
    """
    _flood_fill_name = u"Stack based flood fill"

    @plot_timing
    def fill(self, x, y, color):
        selected_pixel_sign = self.pixels[x][y]
        stack = [(x, y)]
        while stack:
            x, y, stack = stack[0][0], stack[0][1], stack[1:]
            if self.pixels[x][y] == selected_pixel_sign:
                self.pixels[x][y] = color
                if x > 0:
                    stack.append((x - 1, y))
                if x < len(self.pixels) - 1:
                    stack.append((x + 1, y))
                if y > 0:
                    stack.append((x, y - 1))
                if y < len(self.pixels[x]) - 1:
                    stack.append((x, y + 1))
        return self


class Solution3(Canvas):
    """
    Quick executing decision implemented with scipy package with a usage of ndimage.label for a flood fill algorithms
    It should defenitely work faster than previous algorithms for big scales 
    due to strong C++ relization of numpy structures and labeling algorithm
    """
    _flood_fill_name = u"SciPy API based flood fill"
    
    @plot_timing
    def fill(self, x, y, color):
        pixels_matrix = numpy.array(self.pixels)
        pointed_pixel = pixels_matrix[x,y]
        pixels_matrix[pixels_matrix != pointed_pixel] = 0
        pixels_matrix[pixels_matrix == pointed_pixel] = 1
        pixel_borders = pixels_matrix.astype(int)
        filtered_pixels, _labeled = label(pixel_borders)
        filtered_pixels = filtered_pixels.astype(str)
        filtered_pixels[filtered_pixels == filtered_pixels[x,y]] = color
        final_array = numpy.array(self.pixels).astype(str)
        numpy.copyto(final_array,filtered_pixels,'unsafe',filtered_pixels == color)
        self.pixels = final_array.tolist()
        return self


def test_solution(impl):
    s = impl([
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'O', '#', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', '#', '#'],
        ['X', 'X', 'X', 'X', 'X']
    ])
    s.fill(0, 1, '*')
    s.fill(5, 4, 'O')
    s.fill(2, 2, '@')
    print "Comparable string: \n"+str(s)
    print "Compare to: \n" + 'O****\n*OOO*\n*O@O*\n*OOO*\n*****\n***OO\n*****'
    assert str(s) == 'O****\n*OOO*\n*O@O*\n*OOO*\n*****\n***OO\n*****'


if __name__ == '__main__':
    test_solution(Solution1)
    test_solution(Solution2)
    #additional numpy,scipy decision
    test_solution(Solution3)
    #Additional calls to plot execution time of solutions
    plt.plot(timing_results, 'ro')
    plt.ylim(0, numpy.max([el[1] for el in timing_results]))
    plt.xlim(0, numpy.max([el[0] for el in timing_results]))
    plt.show()
