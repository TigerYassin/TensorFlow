import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a * 2

dictionary = {a: [ [1,2,3],[4,5,6], [7,8,9], [10,11,12]  ,      [ 13, 14, 15], [16, 17, 18], [19,20,21] ]}

with tf.Session() as sess:
    result = sess.run(c, feed_dict=dictionary)
    print(result)























import tensorflow as tf

Placeholder1 = tf.placeholder(tf.float16)
Placeholder2 = tf.placeholder(tf.float16)

adding = tf.add(Placeholder1, Placeholder2)

with tf.Session() as session:
    print(session.run(Placeholder1, {Placeholder1: 10}))                #the value of the placeholder must be provided each time
    print(session.run(adding, feed_dict={Placeholder1: 12, Placeholder2: 2}))   #the feed dict is optional





print('\n')






















import tensorflow as tf

Place1 = tf.placeholder(tf.float32)
Place2 = tf.placeholder(tf.float32)

multiply = Place1 * Place2

Array1 = [  [12, 23,3], [3,4, 19], [2, 8, 21]  ]
Array2 = [  [1, 2, 3,], [1, 2, 3], [1, 2, 3]   ]


with tf.Session() as session:
    print(session.run(multiply, feed_dict={Place1: Array1, Place2: Array2}))


