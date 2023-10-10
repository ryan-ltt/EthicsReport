# Title:    DRAWING GRAPHS FOR ETHICS ASSIGNMENT (CHATGPT SURVEY)
# Names:    Zaheer Dhalla - 501170756
#           Ryan Little - 501183218
#           Ethan Chernitzky - 501179991
# Date:     Saturday, April 1st, 2023

# Importing the matplotlib.pyplot function in order to create graphs
import matplotlib.pyplot as plt

# Importing pandas in order to manipulate excel data from our survey
import pandas as pd

# Reading the csv file which contains all of the data from the survey responses
allData = pd.read_csv("ethicsResponses.csv")


# Accessing the columns that have the responses and converting them into python lists
# The built-in .iloc pandas function returns that corresponding column in the form of a 
# Special type called a Series, which is then converted into a list using the tolist() method
# Which is a built-in function for panda series'
genderData = allData.iloc[:,1].tolist()
occupationData = allData.iloc[:, 2].tolist()
ageData = allData.iloc[:, 3].tolist()
institutionData = allData.iloc[:, 4].tolist()
livingData = allData.iloc[:, 5].tolist()
usageFrequencyData = allData.iloc[:,6].tolist()
waysItsUsedData = allData.iloc[:,7].tolist()
aidingStudentsData = allData.iloc[:,8].tolist()
acceptedInAcademiaData = allData.iloc[:,9].tolist()


# This function counts the number of times a certain response has come up
# The information is saved into a dictionary
def frequencyCounter(arr, sort=True):
    dictionary = dict()
    
    # Iterating through a list to add all of its unique elements to a dictionary with a counter(key = element, value = frequency)
    for elem in arr:
        elem = str(elem)
        if elem.find(',') == -1:
            dictionary[elem] = dictionary.get(elem,0)+1
        # If a comma is found in the response, it means there were multiple answers chosen so, each answer seperated by a comma will be isolated with the .split() function
        else:
            allElems= elem.split(", ")
            # Adding all of the options seperated by a comma to the dictionary
            for elem in allElems:
                dictionary[elem] = dictionary.get(elem,0)+1
    # If the dictionary is to be sorted by value (which is done by default), then do so using the sort parameter
    if (sort):
    # Returning a dictionary that is sorted by values rather than keys using a lambda function as the key argument in the sorted() method
        return dict(sorted(dictionary.items(), key=lambda item: item[1]))
    # Otherwise, sort the dictionary by keys
    return dict(sorted(dictionary.items()))


# This function takes the sorted dictionary from the previous function
# And converts it into 2 lists, labels and label values which will be used for graphing

def generateLists(dictionary):
    # Declaring 2 empty lists for the labels and labelValues that will be added 
    labels = []
    labelValues = []
    
    # Iterating through all of the keys in the dictionary passed in
    for key in dictionary:
        # Appeding the current key to the labels list
        labels.append(key)
        
        # Appending the current value associated with the key to the labelValues list
        labelValues.append(dictionary.get(key))
        
    # Returning both of the lists above in the form of a 2D array
    # The first element of the 2d array is the list of labels, and the 
    # Second element is the list of corresponding values
    return [labels, labelValues]


# THE FOLLOWING FUNCTIONS ARE USED TO CLEAN THE DATA FROM SOME OF THE RESPONSES. SO, IF THE SAME RESPONSE WAS TYPED IN MANY DIFFERENT WAYS,
# IT WOULD GENERALIZE ALL OF THOSE RESPONSES AS 1 LABEL RATHER THAN MANY
def cleanInstitutionData():
    for i in range(len(institutionData)):
        institutionData[i] = institutionData[i].strip()
        elem = institutionData[i].lower()
        if elem == "tmu" or elem == "toronto metropolitan university" or elem == "school (toronto met)" or elem == "toronto met u" or elem == "toronto met" or elem == 'tmpoo':
            institutionData[i] = "Toronto Metropolitan University"
        elif elem == 'uoft' or elem == "university of toronto" or elem == 'utsc':
            institutionData[i] = "University of Toronto"
        elif elem == 'university of waterloo' or elem == 'waterloo' or elem == 'uwaterloo':
            institutionData[i] = 'University of Waterloo'
        elif elem == 'school' or elem == 'school' or elem == 'high school' or elem == 'school ?' or elem == 'school and work part time at a company' or elem == 'school of hard knocks' or elem == 'birchmount park':
            institutionData[i] = "Undisclosed High Schools"
        elif elem == 'rh king academy' or elem == "rh king" or elem == "r.h. king academy" or elem == "r. h. king academy (high school)" or elem == 'r.h.king' or elem == "r.h king academy":
            institutionData[i] = "R.H. King Academy"
        elif elem == 'ontario tech':
            institutionData[i] = "Ontario Tech University"
        elif elem == 'mcmaster' or elem == "mcmaster univrrsity" or elem == "mcmaster university":
            institutionData[i] = 'McMaster University'
        elif elem == 'richmond hill high school' or elem == 'richmond green ss':
            institutionData[i] = "Richmond Hill High School"
        elif elem == 'george brown college' or elem == 'george brown':
            institutionData[i] = "George Brown College"
        elif elem == 'uottawa':
            institutionData[i] = "University of Ottawa"
        elif elem == 'laurier':
            institutionData[i] = 'Wilfrid Laurier University'
        elif elem == 'company' or elem == "consulting company":
            institutionData[i] = 'Undisclosed Companies'
            
# Cleaning all the livingSituation data
def cleanLivingData():
    for i in range(len(livingData)):
        livingData[i] = livingData[i].strip()
        elem = livingData[i].lower()
        if elem == 'living with sisters' or elem == 'yurt':
            livingData[i] = "Staying with immediate family"
        elif elem == 'residence' or elem == 'living with a roomate in residence':
            livingData[i] = 'Live with friends'
        elif elem == '2 randoms' or elem == 'dorm with stranger':
            livingData[i] = 'Live with Strangers'
            
# Cleaning the frequency of usage information
def cleanFrequencyUsageData():
    for i in range(len(usageFrequencyData)):
        if usageFrequencyData[i] == "I've never used ChatGPT":
            usageFrequencyData[i] = "Never Used ChatGPT"
        elif usageFrequencyData[i] == "I've never heard of ChatGPT":
            usageFrequencyData[i] = "Never Heard of ChatGPT"
        
# Cleaning the "howItsUsed" data
def cleanHowItsUsedData():
    for i in range(len(waysItsUsedData)):
        waysItsUsedData[i] = str(waysItsUsedData[i])
        if waysItsUsedData[i] == "nan" or waysItsUsedData[i] == "i just said i dont" or waysItsUsedData[i] == 'never used so N/A' or waysItsUsedData[i] == "I don't used it " or waysItsUsedData[i] == "I don't":
            waysItsUsedData[i] = "N/A"
            
# Cleaning the data from the aidingStudents responses
def cleanAidingStudentsData():
    for i in range(len(aidingStudentsData)):
        if aidingStudentsData[i] == "Harming" or aidingStudentsData[i] == "Aiding":
            continue
        else:
            aidingStudentsData[i] = "Other"
            
# Cleaning the data from the question about whether ChatGPT should be accepted in Academia
def cleanAcceptedInAcademia():
    for i in range(len(acceptedInAcademiaData)):
        if (acceptedInAcademiaData[i] == "Yes" or acceptedInAcademiaData[i] == "No"):
            continue
        else:
            acceptedInAcademiaData[i] = "Unsure"
            
# This function is used to format the labels that are shown in some of the graphs.
# It takes a label and slaps the value next to it
def organizeLegendLabels(graphData):
    legendLabels = []
    for i in range(len(graphData[0])):
        legendLabels.append(graphData[0][i] + " - " + str(graphData[1][i]))
    return legendLabels
            
            
# Calling all of the functions that clean the data
cleanInstitutionData()
cleanLivingData()
cleanFrequencyUsageData()
cleanHowItsUsedData()
cleanAidingStudentsData()
cleanAcceptedInAcademia()

#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#
# DRAWING ALL THE GRAPHS USING MATPLOTLIB FUNCTIONS

#----------------------#
# Pie Chart for Genders

properGenderData = frequencyCounter(genderData)
genderGraphData = generateLists(properGenderData)

# Declaring color list
colors = ['r','g','b','m','c']

# Using built-in function from matplotlib to graph a pie chart with the information above
plt.pie(genderGraphData[1], colors = colors, startangle = 90, shadow = True, explode = (0,0,0,0,0.1), radius = 1.2)

# Adding a title to the chart
plt.title("Gender of Respondants\n\n")
    
plt.legend(labels = organizeLegendLabels(genderGraphData), bbox_to_anchor=(1,0))

# Showing the Chart
plt.show()

#----------------------------------------------------#
# Bar Graph for current occupations

properOccupationData = frequencyCounter(occupationData)
occupationGraphData = generateLists(properOccupationData)
colors = ['#E3B22F','#E58B58', '#B57AB0']

# Using built-in function from matplotlib to graph a bar graph with the information above
plt.bar([1,2,3], occupationGraphData[1][::-1], tick_label = occupationGraphData[0][::-1], width = 0.8, color = colors)

# Labeling all axes and title
plt.xlabel('Occupations')
plt.ylabel('Number of People')
plt.title('Current Occupations')

# Built-in function to output the graph
plt.show()

#----------------------------------------------------#
# Bar Graph for Age Ranges

properAgeData = frequencyCounter(ageData, False)
ageGraphData = generateLists(properAgeData)

# Declaring color list
colors = ['#3C86A5', '#80135A','#137960', '#2C135B', '#F2ACB0', '#A56128']

# Using built-in function from matplotlib to draw a bar graph with the information above 
plt.bar([1,2,3,4,5,6], ageGraphData[1], tick_label = ageGraphData[0], width = 0.8, color = colors)
  
# Labeling axes and title
plt.xlabel('Age Ranges')
plt.ylabel('Number of People')
plt.title('Age of Respondants')
  
# Built-in function to output the graph
plt.show()

#----------------------------------------------------#
# Horizontal Bar Graph for Institutions

properInstitutionData = frequencyCounter(institutionData)
institutionGraphData = generateLists(properInstitutionData)

colors = ['#6e0335','#07c252', '#8b37a8', '#ec1e9c', '#6e3722', '#1a2fea', '#21240d','#846dc9','#10dae8', '#e1594b', '#8995e5', '#f25b21', '#d6212c', '#1b8db8', '#103875', '#c6c00e', '#8d7539', '#324d47', '#e88f2a', '#435c72', '#aa4700']


# Using built-in matplotlib function to draw a horizontal bar graph with the info above
plt.barh(institutionGraphData[0], institutionGraphData[1], color=colors)

# Labeling the axes and title
plt.title("Institutions of Respondants")
plt.ylabel("Institutions")
plt.xlabel("Number of People")

# Built-in function to output the graph
plt.show()

#----------------------------------------------------#
# Pie chart for living situations
properLivingData = frequencyCounter(livingData)
livingGraphData = generateLists(properLivingData)

colors = ['#00BB2D', '#F80000', '#C7B446', '#F44611', '#063971']

# Using built-in function from matplotlib to draw a pie chart with the info above
plt.pie(livingGraphData[1], colors = colors, startangle=150, explode = (0,0,0,0,0.1), shadow=True)

# Titling the pie chart
plt.title("Current Living Situations")

plt.legend(labels = organizeLegendLabels(livingGraphData), bbox_to_anchor=(1,0))
# Built-in function to output the graph
plt.show()

#----------------------------------------------------#
# Pie chart for frequency of usage

properUsageFrequencyData = frequencyCounter(usageFrequencyData)
usageFrequencyGraphData = generateLists(properUsageFrequencyData)


plt.pie(usageFrequencyGraphData[1], labels = usageFrequencyGraphData[0], startangle=170, explode = (0,0,0,0,0,0.1), autopct="%1.1f%%")
plt.title("Frequency of Usage")
plt.show()

#----------------------------------------------------#
# Bar graph for how ChatGPT is used

properWaysItsUsedData = frequencyCounter(waysItsUsedData)
waysItsUsedGraphData = generateLists(properWaysItsUsedData)

# Declaring color list
colors = ['r','c','y','g','b','m']

# Using built-in function from matplotlib to create a horizontal bar graph with the info above
plt.barh(waysItsUsedGraphData[0], waysItsUsedGraphData[1], color=colors)

# Labeling axes and title
plt.ylabel('Tasks Used For')
plt.xlabel('Number of People')
plt.title('How People Use ChatGPT')

# Built-in function to output the graph
plt.show()

#----------------------------------------------------#
# Pie chart regarding whether ChatGPT is aiding students

properAidingStudentsData = frequencyCounter(aidingStudentsData)
aidingStudentsGraphData = generateLists(properAidingStudentsData)

# Declaring a color list
colors = ['#62B4B6', '#6E42E7', '#E92353']

# Using built-in function from matplotlib to draw a pie chart with the info above
plt.pie(aidingStudentsGraphData[1], labels = aidingStudentsGraphData[0], startangle=50, explode = (0,0,0.1), autopct = '%1.1f%%', colors = colors, shadow=True)

# Titling the pie chart
plt.title("Is ChatGPT Aiding or Harming Students?")

# Built-in function to output the graph
plt.show()

#----------------------------------------------------#
# Pie chart surrounding whether ChatGPT should be used in Academia

properAcceptedInAcademiaData = frequencyCounter(acceptedInAcademiaData)
acceptedInAcademiaGraphData = generateLists(properAcceptedInAcademiaData)

# Declaring color list
colors = ['#57A639', '#1B5AEA', '#D84B20']

# Using built-in function from matplotlib to draw a pir chart with the information above
plt.pie(acceptedInAcademiaGraphData[1], labels = acceptedInAcademiaGraphData[0], startangle=60, explode = (0,0,0.1), autopct = '%1.1f%%', colors = colors, shadow=True)
# Titling the pie chart
plt.title("Should ChatGPT be a Tool Accepted in Academia?")

# Built-in function to output the graph
plt.show()








        

        






