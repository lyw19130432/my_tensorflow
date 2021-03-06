import tensorflow as tf;
import numpy as np;

def train_data():
    x = [[0.2], [0.4], [0.7], [1.2], [1.4], [1.8], [1.9], [2], [0.11], [0.16], [0.5]];

    y = [[1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [1, 0], [1, 0]];
    return (x, y);

def test_data():
    x = [[0.3], [0.6], [0.8], [1.3], [1.5]];
    y = [[1, 0], [1, 0], [1, 0], [0, 1], [0,1]];
    return (x, y);


x = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='x-input');
y_ = tf.placeholder(dtype=tf.float32, shape=[None, 2], name='y-input');

w1 = tf.get_variable('weight1', shape=[1, 3],
        initializer=tf.random_normal_initializer(stddev=1, dtype=tf.float32))
b1 = tf.get_variable('biase1', shape=[3],
        initializer=tf.random_normal_initializer(stddev=1, dtype=tf.float32))
w2 = tf.get_variable('weight2', shape=[3, 2],
        initializer=tf.random_normal_initializer(stddev=1, dtype=tf.float32))
b2 = tf.get_variable('biase2', shape=[2],
        initializer=tf.random_normal_initializer(stddev=1, dtype=tf.float32))

layer1 = tf.nn.sigmoid(tf.matmul(x, w1) + b1);
y = tf.matmul(layer1, w2) + b2;

loss = tf.nn.l2_loss(y-y_);

train_op = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss);

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer());
    x_train = train_data()[0];
    y_train = train_data()[1];
    for i in range(10000):
        sess.run(train_op, feed_dict={x:x_train, y_:y_train})

    x_test = test_data()[0];
    y_test = test_data()[1];

    count = 0;
    y_max_value_index = np.argmax(y_test, axis=1);
    for i in range(5):
        y_value = sess.run(y[i], feed_dict={x:x_test});

        if np.equal(y_max_value_index[i], np.argmax(y_value)):
            count += 1;
    print("the right proportion: %f"%(count/len(y_test)));



























