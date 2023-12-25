for i in range(40):
    #all_features = tf.reshape(all_features,shape=(,7))
    x = layers.Dense(i+1, activation="relu")(all_features)
    x = layers.Dropout(0.5)(x)
    output = layers.Dense(1, activation="relu")(x)
    model = keras.Model(all_inputs, output)
    model.compile("adam", "binary_crossentropy", metrics=["mse"])
    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0)


    model.summary()
    #model.fit(train_ds, epochs=50,validation_data=val_ds, callbacks=[tensorboard_callback])


    history = model.fit(train_ds, epochs=80, validation_data=val_ds,callbacks=[tensorboard_callback])

    things.append([i,history])

things = sorted(things, key=lambda x: x[1].history['val_mse'][-1])

for i in things:
    print(i[0],i[1].history['val_mse'][-1])

exit()