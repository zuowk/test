import tensorflow as tf
hello=tf.Constant('hello')
with tf.Session() as sess:
  print(sess.run(hello))
