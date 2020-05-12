#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 05:08:57 2020

@author: Lukas Baur
"""

import global_code
import saving
import matplotlib.pyplot as plt 



def plot_q3(y, wbar, tmax, dimensions):
    M = y.reshape(dimensions)
    M = global_code.rescale_to_pixel_representation(M)
    fig, ax = plt.subplots()
    _ = ax.imshow( M, cmap='binary_r', interpolation='nearest')
    path =  '{}q3/tmax{}_wbar{}.png'.format(global_code.IMG_OUTPUT_PATH, tmax, wbar)
    save_img(path)
    plt.title('Sample for w_ij = {}, b_i = 0 (t_max = {})'.format(wbar, tmax))
    plt.show()
    
    
    
def plot_mixing_times(run_avg_curves, w_bars, runs, question, order):
    for i,run_avg in enumerate(run_avg_curves):
        plt.plot(run_avg, label='wij={}'.format(w_bars[i]))
       
    path =  '{}{}/runs{}_diff_wbars{}_mixing{}.png'.format(global_code.IMG_OUTPUT_PATH, question, runs, len(run_avg_curves), order)
    plt.title('avg. value for y over time for different w (order:{})'.format(order))
    plt.ylabel('avg. value for y (mean from {} trials)'.format(runs))
    plt.xlabel('iteration')
    plt.legend(loc='upper right')
    save_img(path)
    plt.show()

def plot_img(title, M, save_img_at=None): 
    M = global_code.rescale_to_pixel_representation(M)
    print(M)
    fig, ax = plt.subplots()
    _ = ax.imshow(M, cmap='binary_r', interpolation='nearest')
    plt.title(title)
    if(save_img_at != None):
        save_img(save_img_at)
    plt.show()
    
def save_img(path):
    plt.savefig(path, bbox_inches='tight')
    
def plot_contours(range0, range1, results):

    plt.figure(figsize=(10,12))
    cs = plt.contourf(range1, range0, results,levels=15)
    plt.clabel(cs, inline=0, fontsize=15, colors='#ffffff')
    plt.title('per-pixel-differences for different thetas')
    
    plt.xlabel('thetha 2')
    plt.ylabel('thetha 1')
#    plt.plot(0.3, 0.5, 'ro')

def plot_w_development(w_development):
    plt.figure(figsize=(15,7))
    count = len(w_development)
    for i in range(count):
        plt.plot(w_development[i], label='{}th w coordinate'.format(i))
    plt.title('w entries over time')
    plt.legend()
    plt.xlabel('iteration')
    plt.ylabel('value')
    path =  '{}w_evolution_.png'.format(global_code.IMG_OUTPUT_PATH)
    save_img(path)
    plt.show()

def plt_error_rates(time_steps, error_rates, eps):
    print(time_steps)
    print(error_rates)
    print(eps)
    plt.figure(figsize=(15, 7))
    count = len(error_rates)
    for i in range(count):
        plt.plot(time_steps, error_rates[i], label='stepsize={}'.format(eps[i]))
    plt.title('error rate over time')
    plt.legend()
    plt.xlabel('iteration')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('average error rate')
    path = '{}errer_rates_eps.png'.format(global_code.IMG_OUTPUT_PATH)
    save_img(path)
    plt.show()


def plot_board(board, plot_name, number_cluster, function_name):
    n,m = board.shape
    scale = 25
    plt.figure()
    plt.matshow(board, cmap='jet')
    save_img(global_code.IMG_OUTPUT_PATH + str(number_cluster) + '/' + plot_name + '_' + function_name)
