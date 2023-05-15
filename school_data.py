# school_data.py
# HOORIYA AMJAD, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.

import numpy as np
import matplotlib.pyplot as plt

class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):                                                                 # pass in school name and school code 
        self.name = name                                                                            
        self.code = code                                                                            

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))                    # print school name and school code


# IMPORT CSV FILE DATA
data_2020 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)          # 2020-2021 numoy array data
data_2019 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)          # 2019-2019 numpy array data
data_2018 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)          # 2018-2019 numpy array data

# SCHOOL LISTS AND DICT
school_codes = ['1224', '1679', '9626', '9806', '9813', '9815', '9816', '9823', 
'9825', '9826', '9829', '9830', '9836', '9847', '9850', '9856', '9857', '9858', '9860', '9865']     # school codes list

school_names = ['Centennial High School', 'Robert Thirsk School', 'Louise Dean School', 
'Queen Elizabeth High School', 'Forest Lawn High School', 'Crescent Heights High School',
'Western Canada High School', 'Central Memorial High School', 'James Fowler High School',
'Ernest Manning High School', 'William Aberhart High School', 'National Sport School',
'Henry Wise Wood High School', 'Bowness High School', 'Lord Beaverbrook High School',
'Jack James High School', 'Sir Winston Churchill High School', 'Dr. E.P. Scarlett High School',
'John G Diefenbaker High School', 'Lester B. Pearson High School']                                  # school names list

school_dict = dict(zip(school_codes, school_names))                                                 # school dictionary, key: code, value: name

# MAIN FUNCTION
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    print('Array data for 2018-2019')
    print(data_2018)                                                                                # print 2018-2019 array data
    print()
    print('Array data from 2019-2020')
    print(data_2019)                                                                                # print 2019-2020 array data
    print()
    print('Array data from 2020-2021')
    print(data_2020)                                                                                # print 2020-2021 array data

    user_input = input('Please enter high school name or school code: ')                            # prompt user for school name or school code
    
    while not user_input in school_dict.keys() and user_input not in school_dict.values():          # while user input is not a school code or school name in dict:
        print('Please enter valid school name or school code')                                      # request for valid school code or name
        user_input = input('Please enter high school name or school code: ')

    mean_array = (data_2018 + data_2019 + data_2020) // 3                                           # average array of csv files for mean grade value
    graduates_array = (data_2018 + data_2019 + data_2020)                                           # sum array of csv files for total graduates

    if user_input in school_dict.keys():                                                            # if user input is school code in dict keys
        school_name = school_dict.get(user_input)                                                   # get school name from dict, key: user input                          
        name_and_code = School(school_name, user_input)                                             # pass in school_name and user_input to School class
        code_index = school_codes.index(user_input)                                                 # get index of input in codes list
    
    if user_input in school_dict.values():                                                          # if user input is school name in dict values
        school_code = school_codes[school_names.index(user_input)]                                  # get school code using user input index in names list
        name_and_code = School(user_input, school_code)                                             # pass in user_input and school_code to School class
        code_index = school_names.index(user_input)                                                 # get index of input in names list

    print("\n***Requested School Statistics***\n")

    name_and_code.print_all_stats()                                                                 # call print_all_stats function

    grade_10 = int(mean_array[code_index, 1])                                                       # get grade 10 average from mean array for requested school
    grade_11 = int(mean_array[code_index, 2])                                                       # get grade 11 average from mean array for requested school
    grade_12 = int(mean_array[code_index, 3])                                                       # get grade 12 average from mean array for requested school
    graduates = int(graduates_array[code_index, 3])                                                 # get graduates from graduates array for requested school

    print('Mean enrollment for Grade 10:', grade_10)                                                # print average grade 10 
    print('Mean enrollment for Grade 11:', grade_11)                                                # print average grade 11 
    print('Mean enrollment for Grade 12:', grade_12)                                                # print average grade 12 
    print('Total number of graduates from past three years:', graduates)                            # print graduates 
    print()

    # REQUESTED GRADE DATA
    year_2018_10 = int(data_2018[code_index, 1])                                                    # get grade 10s in 2018-2019 data for requested school 
    year_2018_11 = int(data_2018[code_index, 2])                                                    # get grade 11s in 2018-2019 data for requested school
    year_2018_12 = int(data_2018[code_index, 3])                                                    # get grade 12s in 2018-2019 data for requested school

    year_2019_10 = int(data_2019[code_index, 1])                                                    # get grade 10s in 2019-2020 data for requested school
    year_2019_11 = int(data_2019[code_index, 2])                                                    # get grade 11s in 2019-2020 data for requested school
    year_2019_12 = int(data_2019[code_index, 3])                                                    # get grade 12s in 2019-2020 data for requested school

    year_2020_10 = int(data_2020[code_index, 1])                                                    # get grade 10s in 2020-2021 data for requested school
    year_2020_11 = int(data_2020[code_index, 2])                                                    # get grade 11s in 2020-2021 data for requested school
    year_2020_12 = int(data_2020[code_index, 3])                                                    # get grade 12s in 2020-2021 data for requested school

    # MAIN PLOT
    x_points = [10, 11, 12]
    x_axis = range(len(x_points))
    plt.xticks(x_axis, x_points)                                                                    # plot points 10, 11, 12 on x axis of main graph 

    mainplot_2018 = np.array([year_2018_10, year_2018_11, year_2018_12])                            # 2018-2019 grade 10-12 enrollment numpy array
    mainplot_2019 = np.array([year_2019_10, year_2019_11, year_2019_12])                            # 2019-2020 grade 10-12 enrollment numpy array
    mainplot_2020 = np.array([year_2020_10, year_2020_11, year_2020_12])                            # 2020-2021 grade 10-12 enrollment numpy array

    plt.plot(x_axis, mainplot_2018, 'o', label = '2019 enrollment', color = 'red')                  # plot 2018-2019 grade 10-12 enrollment on main graph
    plt.plot(x_axis, mainplot_2019, 'o', label = '2020 enrollment',  color = 'green')               # plot 2019-2020 grade 10-12 enrollment on main graph
    plt.plot(x_axis, mainplot_2020, 'o', label = '2021 enrollment', color = 'blue')                 # plot 2020-2021 grade 10-12 enrollment on main graph

    plt.gcf().set_size_inches(10, 6)                                                                # main graph size
    plt.legend(loc = 'upper left')                                                                  # legend on upper left corner of graph
    plt.title('Grade Enrollment By Year')                                                           # main graph title
    plt.xlabel('Grade Level')                                                                       # x axis label
    plt.ylabel('Number of Students')                                                                # y axis label
    plt.show()                                                                                      # show main graph

    # BONUS
    subplot_x_points = [2019, 2020, 2021]
    subplot_x_axis = range(len(subplot_x_points))
    
    # SUBPLOT 1: GRADE 10
    plt.subplot(3, 1, 1)                                                                            # subplot first row
    plt.xticks(subplot_x_axis, subplot_x_points)                                                    # plot points 2019, 2020, 2021 on x axis of subplot 1
    subplot_gr_10 = np.array([year_2018_10, year_2019_10, year_2020_10])                            # grade 10 enrollment per year numpy array
    plt.plot(subplot_x_axis, subplot_gr_10, '--', label = 'Grade 10', color = 'gold')               # plot grade 10 enrollment per year

    plt.legend(loc = 'upper right')                                                                 # legend on upper right corner of subplot 1
    plt.ylabel('Number of Students')                                                                # y axis label
    plt.title('Enrollment by Grade')                                                                # title for subplots

    # SUBPLOT 2: GRADE 11
    plt.subplot(3, 1, 2)                                                                            # subplot second row
    plt.xticks(subplot_x_axis, subplot_x_points)                                                    # plot points 2019, 2020, 2021 on x axis of subplot 2
    subplot_gr_11 = np.array([year_2018_11, year_2019_11, year_2020_11])                            # grade 11 enrollment per year numpy array
    plt.plot(subplot_x_axis, subplot_gr_11, '--', label = 'Grade 11', color = 'magenta')            # plot grade 11 enrollment per year

    plt.legend(loc = 'upper right')                                                                 # legend on upper right corner of subplot 2
    plt.ylabel('Number of Students')                                                                # y axis label

    # SUBPLOT 3: GRADE 12
    plt.subplot(3, 1, 3)                                                                            # subplot third row
    plt.xticks(subplot_x_axis, subplot_x_points)                                                    # plot points 2019, 2020, 2021 on x axis of subplot 3
    subplot_gr_12 = np.array([year_2018_12, year_2019_12, year_2020_12])                            # grade 12 enrollment per year numpy array
    plt.plot(subplot_x_axis, subplot_gr_12, '--', label = 'Grade 12', color = 'cyan')               # plot grade 12 enrollment per year
    
    plt.legend(loc = 'upper right')                                                                 # legend on upper right corner of subplot 3
    plt.ylabel('Number of Students')                                                                # y axis label

    plt.xlabel('Enrollment Year')                                                                   # x axis label for subplots
    plt.gcf().set_size_inches(10, 7)                                                                # subplots size
    plt.show()                                                                                      # show subplots

if __name__ == '__main__':
    main()                                                                                          # call main function