import csv

def main(): 
    # if score_prev != score new: 

    #     scores.append([current_iteration, score])


    scores = [[20, -6], [300, -8]]

    with open("results.csv", 'w', newline='') as output_file:


        writer = csv.writer(output_file)

        # Print(type(series)).
        writer.writerow(['experiment 1'])

        # Iterate over serie dictionaries. 
        for data in scores: 

            print(data)

            # Write info about each serie to a csv file. 
            writer.writerow([data[0], data[1]])

if __name__ == '__main__':
    main()