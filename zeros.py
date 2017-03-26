import tensorflow as tf


val0 = tf.zeros(1, tf.int32) #fills an array of length 1 with '0'
val1 = tf.ones([3,4], tf.int32) #fills an array of length 3 x 4 with '1'


with tf.Session() as sess:
    print(sess.run(val0))
    print('\n')
    print(sess.run(val1))