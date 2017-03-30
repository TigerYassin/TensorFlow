import tensorflow as tf
import numpy as np


#make the fake data
X_data = np.random.rand(100).astype(np.float32)
y_data = (X_data *.2) + .3      #the .2 is the weight and .3 is the bias


#make the structure

Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0)) #slope
biases = tf.Variable(tf.zeros([1])) #y-intercept

y = (Weights * X_data) + biases


#find the loss
loss = tf.reduce_mean(tf.square(y - y_data))

#use the model
train = tf.train.GradientDescentOptimizer(.5) #.5 is how fast each step should be
optimize = train.minimize(loss)


#initialize variables and start the session
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(100):
        sess.run(optimize)
        if _ % 10 ==0:
            print(sess.run(Weights), sess.run(biases))