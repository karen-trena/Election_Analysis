# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who receive votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.
import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#EJERCICIO 1
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

#EJERCICIO 2
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


#EJERCICIO 3
#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")  ##its doing the same as line 10
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)


#FORMA A
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save='analysis/election_analysis2.txt'
outfilemio = open(file_to_save, "w")
outfilemio.write("Holi")
outfilemio.close()


#FORMA B (cleaner code)
file_to_save='analysis/election_analysis.txt'
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World\n")
    txt_file.write("Esto lo lograste \ncon el prrofe\nel 13 de abril")

    # Write three counties to the file.
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")

    txt_file.write("Ar, ")
    txt_file.write("De, ")
    txt_file.write("Jef")

    txt_file.write("Chicago, Toronto, Ottawa")
##############################################################
#3.4.4
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis3.txt")

# 1. Initialize a total vote counter.
total_votes = 0


# Candidate Options (lista)
candidate_options = []

# 1. Declare the empty dictionary. (diccionario)
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    #The variable, file_reader, is referencing the file object, which is stored in memory
    file_reader = csv.reader(election_data)  
    

    # Print each row in the CSV file.
    #We did not see the headers or columns printed because it was fast
    #Each row in the CSV file was printed out as a list.
    #for row in file_reader:
        #print(row)
    #Para imprimir sólo los headers
    #for row in file_reader:
        #print(row[0])

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1  #Básicamente es un contador de filas

# 3. Print the total votes.
#print(total_votes)

        # Print the candidate name from each row.
        candidate_name = row[2] #los candidatos están en la columna 3


# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options: #para imprimir valores unicos de candidatos; si omito esta lista me dará el listado completo en vez de los valores únicos. #To get the unique names in the candidate_options list, we can use an if statement with the not in membership operator to check if the candidate has been added to the list
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

# Print the candidate list.
#print(candidate_options) #me imprimar la lista completa de candidatos

           # 2. Begin tracking that candidate's vote count.
           #When we add candidate_votes[candidate_name] = 0, we're setting each candidate's vote count to zero
            candidate_votes[candidate_name] = 0 #To create each candidate as a key
        candidate_votes[candidate_name] += 1 #para ir contando la cantidad de votos y no me ponga nada más 0; tendrá que tener una identación menos para que el resultado no sea 1´s.





with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)    
    


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            
            #print statement that prints each candidate's name, their vote count, and their percentage of votes
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print the candidate vote dictionary.
    print(candidate_votes)

    #to print out the winning candidate summary.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        #print(winning_candidate_summary)
