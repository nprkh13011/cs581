# Author: Nidhi Parekh
# Pledge: I Pledge My Honor that I have Abided By the Stevens Honor System

#  youtube.py searches YouTube for videos matching a search term and max results
# Each entry is sorted according to 3 analysis sections: 
# (1) Listing the fields in a table - the original/raw data
# (2) highest like percentage (like count/view count) first
# (3) highest number of comments

# To run from terminal window:   python3 youtube.py
# for my case: it only runs as youtube.py, not sure why

from tabulate import tabulate
from googleapiclient.discovery import build      # use build function to create a service object
import csv
import copy
#from colored import fg

# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyAlZqVuiDHe_zvgDlWIXzTM8rLlo59wucY"

API_NAME = "youtube"
API_VERSION = "v3"       # this should be the latest version

#  retrieve the YouTube records matching search term and max

print("----------------------------------------------ASSIGNMENT 3: YOUTUBE API---------------------------------------------------\n")

def search(search_term, search_max):
    print("\n----------------------------------------------PART 1: LIST IN TABLE FORM---------------------------------------------------\n")
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
    search_data = youtube.search().list(q=search_term, part="id,snippet", maxResults=search_max).execute()

    table = []
    # search for videos matching search term;
    for search_instance in search_data.get("items", []):
        if search_instance["id"]["kind"] == "youtube#video":

            # VideoID & Title already provided
            videoId = search_instance["id"]["videoId"]  
            title = search_instance["snippet"]["title"]

            # Views and Likes already provided 
            video_data = youtube.videos().list(id=videoId,part="statistics").execute()
            for video_instance in video_data.get("items",[]):
                viewCount = video_instance["statistics"]["viewCount"]
                #viewCount = (format(int(viewCount), ","))
                if 'likeCount' not in video_instance["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_instance["statistics"]["likeCount"]
                    #likeCount = (format(int(likeCount), ","))    
                
      
            # get Duration of video & comment
            duration = youtube.videos().list(id=videoId,part="contentDetails").execute()
            for video_duration in duration.get("items",[]):
                duration = video_duration["contentDetails"]["duration"]
                
            # get count of Commments
            comments = youtube.videos().list(id=videoId, part="statistics").execute() 
            for video_comments in comments.get("items", []):
                if 'commentCount' not in video_comments["statistics"]:
                    commmentCount = 0
                else:
                    commentCount = video_comments["statistics"]["commentCount"] # its in string format
                    #commentCount = (format(int(commentCount), ","))

            table.append([videoId, viewCount, likeCount, int(commentCount), duration, title])
    commas_table = copy.deepcopy(table) #create deepcopy to be modified
    for i in range(len(table)):
        commas_table[i][1] = format(int(commas_table[i][1]), ",")
        commas_table[i][2] = format(int(commas_table[i][2]), ",")
        commas_table[i][3] = format(int(commas_table[i][3]), ",")

    print(tabulate(commas_table, headers=['Video ID', 'Views', 'Likes', 'Comments', 'Duration', 'Title'], stralign="left"))
        
        # convert raw data into csv file and print it
    with open('output.csv', 'w', encoding='UTF-8') as csvFile:
        data_fields= ('Video ID', 'Views', 'Likes', 'Comments', 'Duration', 'Title')
        csvWriter = csv.DictWriter(csvFile, fieldnames=data_fields, lineterminator='\n')
        csvWriter.writeheader()
        for i in range(len(table)):
            csvWriter.writerow({'Video ID': table[i][0], 'Views':table[i][1], 'Likes':table[i][2], 'Comments': table[i][3], 'Duration':table[i][4], 'Title':table[i][5]})
    return table
#search(search_term, search_max)

def highest_likes_percentage(table):
    print("\n\n----------------------------------------------PART 2: HIGHEST LIKE PERCENTAGE------------------------------------------------\n")
    #iterate through each item -- each video is its own list o
    percentage_table = []
    for item in table: # item is now a list - rest of the list
        views = int(item[1]) # convert into int
        likes = int(item[2])
        if views != 0: # divide by 0 
            # making another column for like percentage
            percentage_table.append([((likes/views) * 100)] + item) # list of list            
            percentage_table.sort(reverse=True) # sort by highest like percentage
            views = (format(int(views), ","))
            likes = (format(int(likes), ",")) # include commas
            for i in range(0, len(percentage_table)): # i guess like_percentage column is added therefore i+1
                percentage_table[i][0] = round(percentage_table[i][0], 3)
    for i,item in enumerate(percentage_table):
        if i == 5: 
             break
        percentage_table[i][2] = (format(int(percentage_table[i][2]), ",")) # views
        percentage_table[i][3] = (format(int(percentage_table[i][3]), ","))
    table2 = copy.deepcopy(percentage_table) #create deepcopy to be modified
    for i in range(0, len(table2)): # for every video in copy
        #remove undesired attributes
        del(table2[i][5])# deletes duration column
        del(table2[i][4])# deletes comment column
        del(table2[i][1])# deletes videoID column

    for i in range(len(table2)):
        table2[i][0] = (str(table2[i][0])+'%')

    print(tabulate(table2, headers=['Like Percentage(%)', 'Views', 'Likes', 'Title'],stralign="left"))


def highest_number_comments(table):
    print("\n\n----------------------------------------------PART 3: HIGHEST NUMBER OF COMMENTS----------------------------------------------\n")
    comment_table = []
    for item in table: # item is now a list - rest of the list
        views = int(item[1]) # convert into int
        comments = int(item[3])
        if comments != 0: # divide by 0 
            # making another column for like percentage
            comment_table.append(item)
        comment_table.sort(key=lambda item: item[3], reverse=True) # sort by highest comment
    for i,item in enumerate(comment_table):
        if i == 5: 
             break
        comment_table[i][1] = (format(int(comment_table[i][1]), ",")) # views
        comment_table[i][3] = (format(int(comment_table[i][3]), ",")) # comments
    table2 = copy.deepcopy(comment_table) #create deepcopy to be modified
    #print(table2)
    for i in range(0, len(table2)): # for every video in copy
        #remove undesired attributes
        del(table2[i][4]) # remove duration
        del(table2[i][2]) # remove likes
        del(table2[i][0]) # remove videoId
    print(tabulate(table2, headers=['Views', 'Comments', 'Title'], stralign="left"))

# output
def main():
    #input
    search_term = input('Search for: ')
    search_max = input('Max Number of Searches: ')
    table = search(search_term, search_max) #stores results in table
    highest_likes_percentage(table)
    highest_number_comments(table)

if __name__ == "__main__":
    main()

