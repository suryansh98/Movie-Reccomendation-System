#importing all classes from tkinter
from tkinter import *
#importing messagebox module from tkinter
from tkinter import messagebox
#Importing class Recommender from Recommender file present in the same directory
from Recommender import Recommender
#Importing class MovieLens from MovieLens file present in the same directory
from MovieLens import MovieLens

#Creating a window called root
root=Tk()

#This function is to load ratings data and returning MovieLens object and ratings dataset
def LoadMovieLensData():
    ml = MovieLens()
    #Loading movie ratings...
    data = ml.loadMovieLensLatestSmall()
    return (ml,data)

(ml,recommendingData) = LoadMovieLensData()

#Creating a recommender object for SVDTopNRecs function to call
recommender = Recommender(recommendingData)

#This function executes when Recommend button is clicked in the UI
def button():
    
    #Checking if userid and No. of Recs fields are emplty
    #If empty displaying a message box
    if e3.get()=="" or e4.get()=="":
        #Deleting previous entry in list box
        listbox.delete(1,END)
        messagebox.showerror("ERROR",'Please fill UserID and No.of Recommendation first')
    else:
        listbox.delete(1,END)
        
        #Calling SVDTopNRecs ehich return recommendations which are stored in recommendations
        recommendations=recommender.SVDTopNRecs(ml,int(e3.get()),int(e4.get()))
        
        #This is used to display the recommendations in the listbox in the UI
        for i in range(len(recommendations)):
            b=str(ml.getMovieName(recommendations[i][0]))+"  |  "+str(round(recommendations[i][1],2))
            listbox.insert((i+2),str(i+1)+"  |  "+b)

#This is used to change window icon    
root.iconbitmap('C:\\Users\\acer\\Desktop\\placment\\projects\\Movie Recommendation System\\movie.ico')

#This is used to change window background
root.configure(background='skyblue')

#this is used to set window min default size
root.minsize(650,650)

#this is used to set window title
root.title("Movie Recommender System")

#This is a textbox which contains the text we have inserted
T=Text(root,height=1,width=30,font=("bold",24),bg="skyblue",bd=0,fg="black")
T.pack()
T.insert(END,'Welcome to Recommendation System')

#this is the first label
l=Label(root,text='Ratings and Movies dataset are here',font=('bold',16),fg="green",bg="skyblue")
l.place(x=80,y=50,width=450,height=25)

#this is the label for entry1
l1=Label(root,text='ratings.csv',font=16,fg="black",bg="skyblue")
l1.place(x=80,y=80,width=95,height=25)

#Entry field for ratings.csv label
e1=Entry(root)
e1.place(x=80,y=105,width=500,height=25)
#inserted default value in this entry field 
e1.insert(0,MovieLens.ratingsPath)

l2=Label(root,text='movies.csv',font=16,fg="black",bg="skyblue")
l2.place(x=80,y=140,width=95,height=25)

e2=Entry(root)
e2.place(x=80,y=165,width=500,height=25)
e2.insert(0,MovieLens.moviesPath)

l3=Label(root,text='User Id:-',font=16,fg="black",bg="skyblue")
l3.place(x=80,y=210,width=80,height=25)

e3=Entry(root)
e3.place(x=170,y=210,width=30,height=25)

l4=Label(root,text='No. of recommendations:-',font=16,fg="black",bg="skyblue")
l4.place(x=80,y=245,width=230,height=25)

e4=Entry(root)
e4.place(x=320,y=245,width=30,height=25)

#this is creating a button Recommend on clicking that button() runs
b=Button(root,text="Recommend",fg="white",bg="blue",padx=2,pady=4,command=button)
b.place(x=250,y=285,width=80,height=25)

lb=Label(root,text="We Recommend:-",font=("bold",16),fg="gray40",bg="skyblue")
lb.place(x=80,y=335,width=180,height=25)

#This is the List Box for displaying recommendations
listbox=Listbox(root,borderwidth=0, highlightthickness=0)
listbox.insert(1,"Sno.  |  Movie Name               |                  Ratings")
listbox.place(x=80,y=385,width=500,height=200)

#This function is responsible for window that comes
#If this is not written then there is no window 
root.mainloop()