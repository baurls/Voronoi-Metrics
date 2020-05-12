#global imports
import numpy as np
import random
import math

#local imports
import saving
import plotting
import global_code


#...........................................................................................
#                                      util functions
#...........................................................................................

class colorPickerUtil:
    @classmethod
    def get_max_distance_colors(cls, n, min=0, max=255):
        slice = (max - min) / (n-1)
        colors = []
        marker_colors = []
        marker_color = max
        for i in range(n):
            colors.append(min + i*slice)
        for i in range(n):
            marker_colors.append(colors[(i+int(n/2)) % n ])
        return colors, marker_colors


class DistanceMetricsUtil:
    @classmethod
    def l2_norm(cls, x, y, xc, yc):
        return (x-xc)**2 + (y-yc)**2
    @classmethod
    def l1_norm(cls, x, y, xc, yc):
        return abs(x-xc) + abs(y-yc)
    @classmethod
    def cube_norm(cls, x, y, xc, yc):
        return abs(x-xc)**3 + abs(y-yc)**3
    @classmethod
    def tetra_norm(cls, x, y, xc, yc):
        return (x-xc)**4 + (y-yc)**4
    @classmethod
    def dirty_l2_norm(cls, x, y, xc, yc):
        return  ((x-xc)**2 + abs(y-yc)**2) * np.random.normal(loc=1, scale=0.25)
    @classmethod
    def infinity_norm(cls, x, y, xc, yc):
        return max( abs(x-xc), abs(y-yc) )

    @classmethod
    def get_all_functions(cls):
        return [cls.l2_norm, cls.l1_norm, cls.cube_norm, cls.tetra_norm, cls.infinity_norm, cls.dirty_l2_norm]

#...........................................................................................
#                                      Voronoi Board
#...........................................................................................

class VoronoiBoard:
    def __init__(self, height=400, width=400, dist_metric=DistanceMetricsUtil.l2_norm):
        self.height = height
        self.width = width
        self.count_cluster = 0
        self.cluster_center = []
        self.cluster_name = []
        self.marker_color = []
        self.board = np.zeros((height, width))
        self.distance_measure = dist_metric
        k = 5
        self.baord_id = global_code.get_random_name_of_length(k)

    def generate_clusters_centers(self, n, method='random'):
        self.count_cluster = n
        self.cluster_center = []
        self.cluster_name = []
        self.marker_color = []
        if method=='random':
            y = random.sample(range(0, self.height), n)
            x = random.sample(range(0, self.width), n)
            cluster_colors, marker_colors = colorPickerUtil.get_max_distance_colors(n)
            for i in range(n):
                self.cluster_center.append( (x[i], y[i]) )
            self.cluster_name = cluster_colors
            self.marker_color = marker_colors
        else:
            raise NotImplemented

    def set_norm(self, norm):
        self.distance_measure = norm

    def run_clustering(self):
        self.board = np.empty((self.height, self.width))
        for x in range(self.width):
            for y in range(self.height):
                self.board[x,y] = self.__get_nearest_center(x,y)
        for i,(xc, yc) in enumerate(self.cluster_center):
            self.board[xc, yc] = self.marker_color[i]
        self.__plot_board()

    def __get_nearest_center(self, x, y):
        distance = np.empty(self.count_cluster)
        for i, (xc,yc) in enumerate(self.cluster_center):
            distance[i] = self.distance_measure(x,y, xc, yc)
        nearest = distance.argmin()
        return self.cluster_name[nearest]

    def __plot_board(self):
        plotting.plot_board(self.board, self.baord_id, self.count_cluster, self.distance_measure.__name__)


#...........................................................................................
#                                Model and main execution
#...........................................................................................

rep = 5

for _ in range(rep):
    board = VoronoiBoard()
    for k in [3,5,7,10,30]:
        board.generate_clusters_centers(k)
        for dist in DistanceMetricsUtil.get_all_functions():
            print('running ' + dist.__name__ + '() ...')
            board.set_norm(dist)
            board.run_clustering()
        print('done')

