import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a * 2

dictionary = {a: [ [1,2,3],[4,5,6], [7,8,9], [10,11,12]  ,      [ 13, 14, 15], [16, 17, 18], [19,20,21] ]}

with tf.Session() as sess:
    result = sess.run(c, feed_dict=dictionary)
    print(result)