# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path, delimiter=",", skip_header=1)

# print("\nData: \n\n", data)

# print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_np = np.array(new_record)
census = np.concatenate((data,new_np),axis=0)

#Code starts here



# --------------
#Code starts here

age = census[:,0]

max_age = max(age)
min_age = min(age)
age_mean = age.mean()
age_std = np.std(age)

print(max_age)

print(min_age)

print(age_mean)

print(age_std)



# --------------
#Code starts here

race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]
print(race_0)
print(race_1)
print(race_2)
print(race_3)
print(race_4)
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)

min_len = len(census)
if len_0 <= min_len:
    min_len = len_0
if len_1 <= min_len:
    min_len = len_1
if len_2 <= min_len:
    min_len = len_2
if len_3 <= min_len:
    min_len = len_3
if len_4 <= min_len:
    min_len = len_4

print(min_len)


minority_race = 3


# --------------
#Code starts here
senior_citizens = census[census[:,0]> 60]

working_hours_sum = np.sum(senior_citizens[:,6])

# print(senior_citi¿zens)
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum/senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high)

print(avg_pay_low)


