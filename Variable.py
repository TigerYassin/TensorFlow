"""
working with variables in tensorflow
i broke it down into sections so that you can comment out sections at a time
"""


import tensorflow as tf

state = tf.Variable([1,2])          # can also use arrays

one = tf.constant([3,2])
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init_op = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init_op)
    print(session.run(state))
    for _ in range(3):
        session.run(update)
        print(session.run(state))








import tensorflow as tf

theVar = tf.Variable(10)
theConstant = tf.constant(2)

add = tf.add(theVar, theConstant)
update = tf.assign(theVar, add)         #The Constant cannot be changed, only a variable is able to be reassigned. Must be a tensorflow variable

init_Var = tf.global_variables_initializer()        #must do this to initialize all the variables, must be done after the variables

with tf.Session() as sess:
    sess.run(init_Var)                              # runs the initializer
    print(sess.run(theConstant))
    print(sess.run(theVar))
    for x in range(5):
        print(sess.run(add))
        print(sess.run(update))




















import tensorflow as tf

theVar = tf.Variable(4)
theConstant = tf.constant(10)

added = tf.add(theVar, theConstant)
new_val = tf.assign(theVar, added)

init_var = tf.global_variables_initializer()

with tf.Session() as sess:            #must instantiate a session
    sess.run(init_var)
    print(sess.run(added))
    print(sess.run(theConstant))    #in order to show readable data, u must run the object in the session
    print(theVar)               # this obeject is not run in the session and it looks confusing
    for x in range(8):
        print(sess.run(new_val))

with tf.Session() as what:      #another session, each session stores its own shit
    what.run(init_var)
    print(what.run(new_val))    # doesn't continue off of the values that were assigned in the previous session, but instead started everything over