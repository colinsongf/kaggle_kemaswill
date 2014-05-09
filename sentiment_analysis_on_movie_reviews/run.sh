params="-w1 5.72214277857 -w0 22.0673076923 -w3 4.73957542442 -w2 1.96099620517 -w4 16.951987834 -t 1 -d 2 -v 10"
prefix="weight_poly2"
train_data="data_libsvm_train"
#Cross Validation
./libsvm_train ${params} ${train_data}

#Train
params="-w1 5.72214277857 -w0 22.0673076923 -w3 4.73957542442 -w2 1.96099620517 -w4 16.951987834 -t 1 -d 2"
./libsvm_train ${params} ${train_data} ${train_data}_${prefix}.model

#Scoring
test_data="data_libsvm_test"
./libsvm_predict ${test_data} ${train_data}_${prefix}.model ${test_data}_${prefix}.output
