def is_peak_at(data, index, w):
    if (index<w):
        return False
    if (index+1>(len(data)-w)):
        return False
    for j in range(1,w+1):
        if data[index]<=data[index-j]:
            return False
        if data[index]<data[index+j]:
            return False
        pass
    return True

   
def count_laps(data, w):
    peak_count = 0
    for i in range(len(data)):
        if is_peak_at(data, i, w):
            peak_count = peak_count + 1
            pass
        pass
    return peak_count

# this is a testing helper function
def tests_for_hr_data(data_and_answers, w):
    all_right = True
    for (data, answers) in data_and_answers:
        # Tell us what we are testing on
        print("Testing with " + str(data) + " with w = " + str(w))
        # first let us check is_peak_at specifically
        for i in range(len(data)):
            # see what our code got
            ans = is_peak_at(data, i, w)
            # compare it to the right answer
            if ans == (i in answers):
                print("Correctly gave " + str(ans) + " for index " + str(i))
            else:
                print("**INCORRECT** for index = " + str(i) + " got " +
                      str(ans) + " but expected " + str(i in answers))
                all_right = False
                pass
            pass
        # Now test count_laps
        count = count_laps(data, w)
        # and compare it to the right answer
        if (count == len(answers)):
            print("Correctly counted " + str(count) + " laps")
        else:
            print("**INCORRECT** lap count, got " + str(count) +
                  " but expected " + str(len(answers)))
            all_right = False
            pass
        pass
    return all_right

# if we run this as the main module, run some test cases on our functions
if __name__ == "__main__":
    # We will start by testing with w = 2
    # The small example data from the video, which has peaks at indices 2 and 8
    data0 = [160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162]
    peaksat0 = [2, 8]
    # The second example from the video, with a "fake" peak at index 6
    data1 = [160, 161, 162, 161, 160, 161, 163, 162, 164, 163, 162]
    peaksat1 = [2, 8]
    # The third example from the video, with three consecutive 164 values
    data2 = [160, 161, 162, 163, 164, 164, 164, 163, 162, 161, 160]
    peaksat2 = [4]
    # Always good to test on the empty list: it has no peaks
    data3 = []
    peaksat3 = []
    # A one element list which has no peaks
    # (we require at least w=2 points on each side)
    data4 = [190]
    peaksat4 = []
    # Still too few points for a peak with w = 2
    data5 = [188, 190, 189]
    peaksat5 = []
    # the smallest list we can make with a peak for w = 2
    data6 = [187, 188, 189, 186, 180]
    peaksat6 = [2]
    # we can make a list of tuples for the data we want to test with for
    # w = 2
    

    w2_data = [(data0, peaksat0), (data1, peaksat1), (data2, peaksat2),
               (data3, peaksat3), (data4, peaksat4), (data5, peaksat5),
               (data6, peaksat6)]
    all_right = tests_for_hr_data(w2_data, 2)
    w1_data = w2_data[:]
    w1_data[1] = (data1, [2, 6, 8])
    w1_data[5] = (data5, [1])
    all_right = tests_for_hr_data(w1_data, 1) and all_right
    w4_data = [(data0, []), (data1, []), (data2, [4]),
               (data3, []), (data4, []), (data5, []),
               (data6, [])]
    all_right = tests_for_hr_data(w4_data, 4) and all_right
    if not all_right:
        print("Failed one or more tests!")
    pass
