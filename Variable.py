# import tensorflow as tf
#
# state = tf.Variable(0)
#
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# init_op = tf.global_variables_initializer()
#
# with tf.Session() as session:
#     session.run(init_op)
#     print(session.run(state))
#     for _ in range(3):
#         session.run(update)
#         print(session.run(state))








import tensorflow as tf

theVar = tf.Variable(10)
theConstant = tf.constant(2)

add = tf.add(theVar, theConstant)

init_Var = tf.global_variables_initializer()        #must do this to initialize all the variables, must be done after the variables

with tf.Session() as sess:
    sess.run(init_Var)                              # runs the initializer
    print(sess.run(theConstant))
    print(sess.run(theVar))
    for x in range(5):
        print(sess.run(add))


