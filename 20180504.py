# -*- coding: utf-8 -*-
"""
Created on Fri May  4 07:34:11 2018

@author: Administrator
"""

import tensorflow as tf
w1=tf.constant([1,2,3])
#w1= tf.Variable(tf.random_normal([2, 3], stddev=1, seed=2))
w2= tf.Variable(tf.random_normal([3, 1], stddev=1, seed=2))
with tf.Session() as sess:
    #sess.run(w1.initializer)
    print(sess.run(w1))