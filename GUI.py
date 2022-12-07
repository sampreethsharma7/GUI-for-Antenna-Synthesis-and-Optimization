# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:07:42 2021

@author: sinf5
"""
import random
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
import data_extraction as DX
import data_extraction_testdata as DXT
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
#from PIL import ImageTk, Image
import pickle
import matplotlib
from matplotlib.animation import FuncAnimation
import xlsxwriter as xl
from tkinter.filedialog import asksaveasfile
from sklearn.metrics import mean_squared_error
import math
from PIL import ImageTk, Image
root = tk.Tk()
W=1800
L=1800
count =0
root.geometry("1800x1800")
root.resizable(True,True)
fnt =("Courier Font",14)
root.title("GUI")
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 12}
#root.attributes('-alpha',0.5)
# Create an object of tkinter ImageTk
midelogo = ImageTk.PhotoImage(Image.open("MicrosoftTeams-image (11).png"))
umkclogo = ImageTk.PhotoImage(Image.open("UMKClogo.png"))
# Create a Label Widget to display the text or Image

label_midelogo = tk.Label(root, image = midelogo).place(x=10,y=10)
label_umkclogo = tk.Label(root, image = umkclogo).place(x=1660,y=10)



matplotlib.rc('font', **font)
root.configure(background='LightSteelBlue2')
#root.wm_attributes('-transparentcolor','white')
def cleartext():
    T.delete("1.0", "end")


# Create text widget and specify size.
T = tk.Text(root, height = 15, width = 100)#width =200/100 for desktop/laptop
T.place(x =400,y=L/4)
mybutton_delete = tk.Button(root, text = "Clear",command=cleartext,padx = 50,pady =2,bg ='brown3')
mybutton_delete.place(x= 1205,y = L/4)#x=1605/1405 for desktop/laptop







def traininginput():
    global training_input_path    
    folder = askdirectory()
    if folder:
        training_input_path = folder
        msg = "Getting training input data "
        T.insert(tk.END, msg + '\n')
        print(training_input_path)
#browsebuttontrainingdata
mybutton_traininginput = tk.Button(root, text = "Load training Input data",command = traininginput,padx = 20,pady =20,fg = 'white',bg ='DodgerBlue3')
mybutton_traininginput.place(x=300,y =100)


def trainingdata():
    global training_output_path 
    folder = askdirectory()
    if folder:
        training_output_path =folder
        DX.listfiles(folder)
        msg = "Getting training output data "
        T.insert(tk.END, msg + '\n')
       
#browsebuttontrainingdata
mybutton_trainingdata = tk.Button(root, text = "Load training output data",command =trainingdata,padx = 20,pady =20,fg = 'white',bg ='DodgerBlue3')
mybutton_trainingdata.place(x=600,y =100)



def testdata():
    global test_output_path 
    folder = askdirectory()
    if folder:
        test_output_path= folder
        DXT.listfiles(folder)
        msg = "Getting test output data "
        T.insert(tk.END, msg + '\n')
#browsebuttontestdata
mybutton_testdata = tk.Button(root, text = "Load test output data",command =testdata,padx = 30,pady =20,fg = 'white',bg ='DodgerBlue3')
mybutton_testdata.place(x=1200,y =100)

"""MenuOptions"""
# Create the list of options
options_list = ["KNN", "LR", "Lasso", "ML4"]

# Variable to keep track of the option
# selected in OptionMenu
value_inside = tk.StringVar(root)

# Set the default value of the variable
value_inside.set("Select an Option")

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = ttk.OptionMenu(root, value_inside, options_list[0],*options_list)
question_menu.place(x= 900, y =304 )
#question_menu.config(background ="LightSteelBlue2")
# Function to print the submitted option-- testing purpose
testoutput = []
outputs = []

def CallingMLmodel():
    global ParameterCount
    global ParameterList
    global df_target
    traininput_filename = filedialog.askopenfilename(initialdir = "/Users/sinf5/Desktop/python", title ="select training input", filetypes=[("Excel files", ".xlsx .xls")])
    df_training_input = pd.read_excel(traininput_filename)
    ParameterCount = df_training_input.shape[1]
    ParameterList = df_training_input.columns.values
    window2.Parameterinfo(ParameterCount,ParameterList)
    trainingoutput_filename = filedialog.askopenfilename(initialdir = "/Users/sinf5/Desktop/python", title ="select training output", filetypes=[("Excel files", ".xlsx .xls")])
    df_training_output = pd.read_excel(trainingoutput_filename)
    df_training_output = df_training_output.T
    # testinput_filename = filedialog.askopenfilename(initialdir = "/Users/sinf5/Desktop/python", title ="select test input", filetypes=[("Excel files", ".xlsx .xls")])
    # df_test_input = pd.read_excel(testinput_filename)
    #df_test_input =df_test_input.T
    
    model = value_inside.get()
    
    if model == 'KNN':
        MLmodel = KNeighborsRegressor(1)
        MLmodel.fit(df_training_input,df_training_output)
        T.insert(tk.END,'success' + '\n')
        validate_button['state'] = tk.NORMAL
        TrainedKnnModel = 'KNR'
        pickle.dump(MLmodel,open(TrainedKnnModel,'wb'))
    elif model == 'LR':
        MLmodel = LinearRegression()
        MLmodel.fit(df_training_input,df_training_output)
        T.insert(tk.END,'success' + '\n')
        validate_button['state'] = tk.NORMAL
        TrainedKnnModel = 'LR'
        pickle.dump(MLmodel,open(TrainedKnnModel,'wb'))
    elif model == 'Lasso':
        MLmodel = Lasso(alpha=0.1)
        MLmodel.fit(df_training_input,df_training_output)
        T.insert(tk.END,'success' + '\n')
        validate_button['state'] = tk.NORMAL
        TrainedKnnModel = 'Lasso'
        pickle.dump(MLmodel,open(TrainedKnnModel,'wb'))
    else :
        T.insert(tk.END,'puff' + '\n')
    
submit_button = tk.Button(root, text='Train the model', command=CallingMLmodel,fg = 'white',bg ='DodgerBlue3')
submit_button.place(x= 1000,y=300)
select = tk.Label(root, text ="Select a machine learning model :",font =fnt,bg ='LightSteelBlue2')
select.place(x =600,y= 300)

class window2:
    Toutput = []
    count =0
    
    def __init__(self): 
        
        self.target_upload = 0
        self.roottemp = tk.Tk()
        self.roottemp.geometry("400x100")
        self.roottemp.resizable(True,True)
        self.roottemp.title("Enter Number of Input's")
        self.myspinbox = tk.Spinbox(self.roottemp,from_ =1,to=10,font =fnt)
        self.myspinbox.grid(row=0,column=1,padx=5,pady=5)
        
        self.callingmain = tk.Button(self.roottemp,text='Next',font =fnt,command=self.inputentry)
        self.callingmain.grid(row=0,column=2,padx=5,pady=5)
        
    def back(self):
            self.roottemp2.destroy()
            self.__init__()
    def inputentry(self):
       
        self.ParameterCountUserInput =   int(self.myspinbox.get())
        self.roottemp.destroy()
        self.roottemp2 = tk.Tk()
        self.roottemp2.resizable(True,True)
        self.roottemp2.geometry("500x500")
        self.roottemp2.title("Enter Input Lables")
        self.BackButton = tk.Button(self.roottemp2,text="Back",command=self.back)
        self.BackButton.grid(row=0,column=0)
        self.ValButton = tk.Button(self.roottemp2,text="Proceed to Validation Window",command=self.mainn)
        self.ValButton.grid(row=0,column=1)
        self.inputdesignparameter =[]
        self.inputname=[]
        for i in range(self.ParameterCountUserInput):
            self.Numofparameters = i+1
            txt = 'Enter the Label for Input '+str(self.Numofparameters)
            Labeldesignparameter = tk.Label(self.roottemp2, text=txt,font =fnt)
            Labeldesignparameter.grid(row=self.Numofparameters,column=0,padx=5,pady=10,columnspan=3)
            self.inputdesignparameterentry = tk.Entry(self.roottemp2, width = 10)#width =200/100 for desktop/laptop
            self.inputdesignparameterentry.grid(row=self.Numofparameters,column=4,padx=5,pady=10,columnspan=3)
            self.inputname.append(self.inputdesignparameterentry)
    def saveequation(self):
        ary=[]
        if self.flag == 0:
            print(self.dfa,111)
            
            self.variable_list = self.dfa.columns.values.tolist()
            print(self.variable_list)
            self.UserEqua=str(self.Equation_AntennaArray.get())
            print(self.UserEqua)
            self.lst = []
            for letter in self.UserEqua:
            	self.lst.append(letter)
            self.newlst= []
        
            Gcount=0
            while Gcount< len(self.lst):
                
                if ((self.lst[Gcount] >= 'A' and self.lst[Gcount] <= 'Z') or (self.lst[Gcount] >= 'a' and self.lst[Gcount] <= 'z')):
                    temp =''
                    print(Gcount,'h')
                    while (Gcount<len(self.lst)) and ((self.lst[Gcount] >= 'A' and self.lst[Gcount] <= 'Z') or (self.lst[Gcount] >= 'a' and self.lst[Gcount] <= 'z')):
                        temp =temp+str(self.lst[Gcount])
                        Gcount=Gcount+1
                    
                    Gcount=Gcount-1
                    self.newlst.append(temp)
                else:   
                    print(Gcount)
                    self.newlst.append(self.lst[Gcount])
                Gcount +=1
            for i in range(len(self.newlst)):
                if self.newlst[i] in self.variable_list:
                    print(True)
                    print(self.newlst[i],"self.dfa['"+str(self.newlst[i])+"'].values[i]")
                    self.newlst[i]="self.dfa['"+str(self.newlst[i])+"'].values[i]"
                    
            print("".join(self.newlst))
            # for i in range(len(self.lst)):
            #     print(i)
            #     if self.lst[i] in self.variable_list:
            #         print(True)
            #         print(self.lst[i],"self.dfa['"+str(self.lst[i])+"'].values[i]")
            #         self.lst[i]="self.dfa['"+str(self.lst[i])+"'].values[i]"
                    
            # print("".join(self.lst))
            self.UserEqua_modified ="".join(self.newlst)     
            for i in range(len(self.dfa)):
                self.parasweep_text.insert(tk.END, 'Physical aperture area calculated using '+ str(self.UserEqua)+ 'is '+str(eval(self.UserEqua_modified)) +' mm\u00b2'+'\n')
                ary.append(eval(self.UserEqua_modified))
            
            self.PhyApertureArea.insert(self.calling_count,'PHY_A_A'+str(self.calling_count), ary)
            ary2 = df.iloc[self.gain_loc,:].tolist()
            self.calling_count+=1
            self.eff =[]
            eff_inp = ary[0]/ary2[0]
            self.loc_array_als =0
            for i in range(len(ary)):
                self.eff.append(ary[i]/ary2[i])
                if self.eff[i]<eff_inp:
                    eff_inp=self.eff[i]
                    self.loc_array_als = i
            self.parasweep_text.insert(tk.END, 'Efficient input is '+ str(self.temp[self.loc_array_als])+ ' with a gain value of '+str(ary2[self.loc_array_als]) +' and a Physcial Aperture area of '+str(ary[self.loc_array_als])+' mm\u00b2'+'\n')
            print(ary,ary2,self.eff,eff_inp)
        elif self.flag==1:
            val = self.shapeselection_SideLen_AntennaArray.get()
            ary=[]
            if self.shapeselection_value_inside.get() == "Square":
                print(type(val))
                if type(val)== str:
                    for i in range(len(self.dfa)):
                        val = val+'[i]'
                        ary.append(eval(val**2))
                elif type(val)==int:
                    for i in range(len(self.dfa)):
                        ary.append(eval(val**2))
                        
                # self.parasweep_text.insert(tk.END, 'Physical aperture area calculated using '+ str(val**2)+ 'is '+str(eval(val**2)) +'\n')
                print(ary,'square')
        #Plotting
        plt.clf()
        x = np.linspace(1,len(self.Toutput),len(self.Toutput))
        figure2 =plt.figure(figsize = (10,8),dpi =100)
        ax=plt.axes()
        figure2.add_subplot(111).plot(x, df.iloc[self.gain_loc,:])
        chart = FigureCanvasTkAgg(figure2,self.root2)
        chart.get_tk_widget().place(x=600,y = 10)
       
        
        #fig, ax = plt.subplots(figsize = (10, 5))
        #plt.title('Example of Two Y labels')
         
        # using the twinx() for creating another
        # axes object for secondary y-Axis
        ax2 = ax.twinx()
        ax.plot(x, ary2, color = 'g')
        ax2.plot(x, ary, color = 'b')
         
        # giving labels to the axises
        ax.set_xlabel('Input No.', color = 'r')
        ax.set_ylabel('Gain (dBi)', color = 'g')
         
        # secondary y-axis label
        ax2.set_ylabel('Physical aperture area (mm\u00b2)', color = 'b')
 
    def antennaarray(self):
        W2=800
        L2=200
        #No. of times user clicked save button (helps in moving the dataframe column in save eqauation function)
        self.calling_count =0
        self.PhyApertureArea =pd.DataFrame()
        self.rootantennaarray=tk.Tk()
        self.rootantennaarray.geometry(f"{W2}x{L2}")
        self.rootantennaarray.resizable(True,True)
        self.rootantennaarray.title("Antenna Array Analysis")
        self.rootantennaarray.configure(background='LightSteelBlue2')
        self.label_Equation_AntennaArray= tk.Label(self.rootantennaarray, text='Enter equation ',font =("Helvetica",14),bg ='LightSteelBlue2')
        self.label_Equation_AntennaArray.grid(row=0,column=0,padx=5,pady=10,columnspan=3)
        self.Equation_AntennaArray = tk.Entry(self.rootantennaarray, width = 40)
        self.Equation_AntennaArray.insert(0, "Enter equation here")
        self.Equation_AntennaArray.grid(row=0,column=4,padx=5,pady=10,columnspan=3)
        self.savebtn = tk.Button(self.rootantennaarray,text="save",command=self.saveequation)
        self.savebtn.grid(row =1,column=3)
        self.flag=0
        # self.Radiobutton(self.rootantennaarray, text = "text", variable = v,value = value)
    def antennaarray_shapeselection(self):
        W2=800
        L2=200
        self.flag=1
        self.rootantennaarrayshapeselection=tk.Tk()
        self.rootantennaarrayshapeselection.geometry(f"{W2}x{L2}")
        self.rootantennaarrayshapeselection.resizable(True,True)
        self.rootantennaarrayshapeselection.title("Antenna Array Analysis")
        self.rootantennaarrayshapeselection.configure(background='LightSteelBlue2')
        self.label_Equation_AntennaArray= tk.Label(self.rootantennaarrayshapeselection, text='Select antenna array shape :',font =("Helvetica",14),bg ='LightSteelBlue2')
        self.label_Equation_AntennaArray.grid(row=0,column=0,padx=5,pady=10,columnspan=3)
        """MenuOptions"""
        # Create the list of options
        self.shapeselection_options_list = ["Square", "Rectangle", "Octogon"]

        # Variable to keep track of the option
        # selected in OptionMenu
        self.shapeselection_value_inside = tk.StringVar(root)

        # Set the default value of the variable
        self.shapeselection_value_inside.set("Select an Option")

        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.
        self.shapeselection_question_menu = ttk.OptionMenu(self.rootantennaarrayshapeselection, self.shapeselection_value_inside, self.shapeselection_options_list[0],*self.shapeselection_options_list)
        self.shapeselection_question_menu.grid(row=0,column=3,padx=5,pady=10,columnspan=5)
        self.shapeselection_question_menu.configure(width = 10)
        self.shapeselection_SideLen_AntennaArray = tk.Entry(self.rootantennaarrayshapeselection, width = 40)
        self.shapeselection_SideLen_AntennaArray.insert(0, "Enter side length here")
        self.shapeselection_SideLen_AntennaArray.grid(row=1,column=4,padx=5,pady=10,columnspan=3)
        self.shapeselection_savebtn = tk.Button(self.rootantennaarrayshapeselection,text="save",command=self.saveequation)
        self.shapeselection_savebtn.grid(row =2,column=3)
    def mainn(self): 
        W2=1800
        L2=1800
        self.root2=tk.Tk()
        self.root2.geometry(f"{W2}x{L2}")
        self.root2.resizable(True,True)
        self.root2.title("validate")
        self.root2.configure(background='LightSteelBlue2')
        self.counter_1 = 0
        my_menu = tk.Menu(self.root2)
        self.root2.config(menu = my_menu)
        
        def Export_command():
            files = [('Excel File', '*xlsx*')]
            file = asksaveasfile(filetypes = files, defaultextension = files)
            # filename = str(file)+".xlsx"
            print("here u see",file.name)
            outputdatatoexcel = pd.ExcelWriter(file.name)
            self.dfdel_global.to_excel(outputdatatoexcel,index=False)
            outputdatatoexcel.save()
            
        def Compare__command():
            rootcompare = tk.Tk()
            rootcompare.geometry("500x500")
            rootcompare.title("Comparision")
            rootcompare.configure(background='LightSteelBlue2')
            plt.close('all')
            
            if bool(self.target_upload) == False:
                self.target_filename = filedialog.askopenfilename(initialdir = "/Users/sinf5/Desktop/python", title ="select test output", filetypes=[("Excel files", ".xlsx .xls")])
                self.target = pd.read_excel(self.target_filename)
            
            x = np.linspace((self.FMin)/10e2,(self.FMax)/10e2,num=len(self.target))
            self.target_upload =+1
            
            
            
            
            fig =Figure(figsize = (8,8),dpi =100)
            plot1 =fig.add_subplot(111)
            plot1.plot(x,self.target,label = "Actual output")
            plot1.plot(x,self.dfdel_global,label = "Predicted output")
            
            canvas = FigureCanvasTkAgg(fig,master= rootcompare)
            canvas.draw()
            canvas.get_tk_widget().pack()
            
            toolbar = NavigationToolbar2Tk(canvas, rootcompare)
            
            toolbar.update()
            
            canvas.get_tk_widget().pack()
            # plot1.xlabel('Frequency (GHz)')
            # if self.value_inside_outputtype.get() == 'Gain':
            #     plot1.ylabel('Gain (dBi)')
            # elif self.value_inside_outputtype.get() == 'S11':
            #     plot1.ylabel('S11 (dB)')
            # elif self.value_inside_outputtype.get() == 'Gain(\u03F4)':
            #     plot1.ylabel('Gain(\u03F4)')
            
            plot1.grid()
            plot1.legend()
        
        #menu item
        file_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Export plot data",command=Export_command)
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        
        #analysis menu item
        analysis_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="Anyalsis",menu=analysis_menu)
        analysis_menu.add_command(label="Compare",command=Compare__command)
        analysis_menu.add_command(label="Error Analysis")
        
        #submenu
        analysis_sub_menu = tk.Menu(my_menu)
        analysis_sub_menu.add_command(label="Select shape",command=self.antennaarray_shapeselection)
        analysis_sub_menu.add_command(label="Custom shape",command = self.antennaarray)
        analysis_menu.add_cascade(label="Antenna Array Analysis",menu = analysis_sub_menu)
        #DesignParameterA
        self.inputvalue =[]
        self.usergivenparanamessaved = []
        for i in range(self.ParameterCountUserInput):
            self.Numofparameters = i+1
            self.usergivenparanamessaved.append(str(self.inputname[i].get()))
            Labeldesignparameter = tk.Label(self.root2, text='Enter value of '+'"'+str(self.usergivenparanamessaved[i])+'"'+':',font =("Helvetica",14),bg ='LightSteelBlue2')
            Labeldesignparameter.grid(row=self.Numofparameters,column=0,padx=5,pady=10,columnspan=3)
            self.inputdesignparameter = tk.Entry(self.root2, width = 10)#width =200/100 for desktop/laptop
            self.inputdesignparameter.grid(row=self.Numofparameters,column=4,padx=5,pady=10,columnspan=3)
            self.inputvalue.append(self.inputdesignparameter)
        # print(self.inputvalue,"hehe")
        self.roottemp2.destroy()
        root.destroy()
        #FrequencyMin
        LabelFMin = tk.Label(self.root2, text ='Frequency minimum:',font =fnt,bg ='LightSteelBlue2')
        LabelFMin.grid(row = self.Numofparameters+1,column=0,padx=5,pady=10)
        self.inputFMin = tk.Entry(self.root2,width = 7)
        self.inputFMin.grid(row = self.Numofparameters+1,column=1,padx=5,pady=10)
        LabelFMin = tk.Label(self.root2, text ='MHz',font =fnt,bg ='LightSteelBlue2')
        LabelFMin.grid(row = self.Numofparameters+1,column=2,padx=5,pady=10)
        
        #FrequencyMax
        LabelFMax = tk.Label(self.root2, text ='Frequency maximum:',font =fnt,bg ='LightSteelBlue2')
        LabelFMax.grid(row = self.Numofparameters+2,column=0,padx=5,pady=10)
        self.inputFMax = tk.Entry(self.root2,width = 7)
        self.inputFMax.grid(row = self.Numofparameters+2,column=1,padx=5,pady=10)
        LabelFMax = tk.Label(self.root2, text ='MHz',font =fnt,bg ='LightSteelBlue2')
        LabelFMax.grid(row = self.Numofparameters+2,column=2,padx=5,pady=10)
        
        #CalculateButton
        calculate_button = tk.Button(self.root2, text='Calculate',command = self.update_parameter_values,fg = 'white',bg ='DodgerBlue3')
        calculate_button.grid(row=self.Numofparameters+3,column=0,columnspan= 2,padx=5,pady=10)
        
        
        #SweepAnalysisButton
        SweepAnalysis_button = tk.Button(self.root2, text='SweepAnalysis',command = self.UserInputParaSweep,fg = 'white',bg ='DodgerBlue3')
        SweepAnalysis_button.grid(row=self.Numofparameters+3,column=1,columnspan= 2,padx=5,pady=10)
        
        #
        
        self.options_list_outputtype = ["S11", "Gain(f)","Gain(\u03F4)"]

        # Variable to keep track of the option
        # selected in OptionMenu
        self.value_inside_outputtype = tk.StringVar(self.root2)
        
        # Set the default value of the variable
        self.value_inside_outputtype.set("Select an Option")
        
        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.
        self.question_menu_outputtype = ttk.OptionMenu(self.root2, self.value_inside_outputtype, self.options_list_outputtype[0],*self.options_list_outputtype)
        self.question_menu_outputtype.grid(row=self.Numofparameters+4,column=1,columnspan= 2,padx=5,pady=10)
        
        self.select_outputtype = tk.Label(self.root2, text ="Select output type :",font =fnt,bg ='LightSteelBlue2')
        self.select_outputtype.grid(row=self.Numofparameters+4,column=0,columnspan= 2,padx=5,pady=10)
        
        self.parasweep_text = tk.Text(self.root2, height = 7, width = 120)#width =200/100 for desktop/laptop
        self.parasweep_text.place(x =600,y=850)
        
        
        
        self.options_list_outputtype_error = ["RMSE", "MSE"]

        # Variable to keep track of the option
        # selected in OptionMenu
        self.value_inside_outputtype_error = tk.StringVar(self.root2)
        
        # Set the default value of the variable
        self.value_inside_outputtype_error.set("Select an error calculation method")
        
        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.
        self.question_menu_outputtype_error = ttk.OptionMenu(self.root2, self.value_inside_outputtype_error, self.options_list_outputtype_error[0],*self.options_list_outputtype_error)
        self.question_menu_outputtype_error.grid(row=self.Numofparameters+5,column=2,columnspan= 2,padx=5,pady=10)
        
        self.select_outputtype_error = tk.Button(self.root2, text ="Calculate error :",command = self.errorcalculation,font =fnt,fg = 'white',bg ='DodgerBlue3')
        self.select_outputtype_error.grid(row=self.Numofparameters+5,column=0,columnspan= 2,padx=5,pady=10)
        
        self.parasweep_text = tk.Text(self.root2, height = 7, width = 120)#width =200/100 for desktop/laptop
        self.parasweep_text.place(x =600,y=850)
        
        
        
        self.root2.mainloop()
        
    def errorcalculation(self):
        if bool(self.target_upload) == False:
            self.target_filename = filedialog.askopenfilename(initialdir = "/Users/sinf5/Desktop/python", title ="select test output", filetypes=[("Excel files", ".xlsx .xls")])
            self.target = pd.read_excel(self.target_filename)
            self.target_upload=+1
        
        if self.value_inside_outputtype_error.get() == 'RMSE':
            RMSE = math.sqrt(mean_squared_error(self.target,self.dfdel_global))
            self.parasweep_text.insert(tk.END, 'RMSE '+ str(RMSE) +'\n')
            print(RMSE)
        elif self.value_inside_outputtype_error.get() == 'MSE':
            
            MSE1 =  mean_squared_error(self.target,self.dfdel_global)
            self.parasweep_text.insert(tk.END, 'MSE '+ str(MSE1) +'\n')
            print(MSE1)
        
    def UserInputParaSweep(self):
        self.count=+1
        #SweepWindow
        self.root3=tk.Tk()
        self.root3.geometry("500x400")
        self.root3.resizable(True,True)
        self.root3.title("Parasweep")
        self.root3.configure(background='LightSteelBlue2')
        self.row6 = 0
        self.row0 = 1
        self.row1 = 2
        self.row2 = 3
        self.row3 = 4
        self.row4 = 5
        self.row5 = 6
        self.row7 = 7
        LabelStart = tk.Label(self.root3, text='Start',font =fnt,bg ='LightSteelBlue2')
        LabelStart.grid(row=1,column=1,padx=5,pady=10)
        Labelend = tk.Label(self.root3, text='End',font =fnt,bg ='LightSteelBlue2')
        Labelend.grid(row=1,column=2,padx=5,pady=10)
        Labelsample = tk.Label(self.root3, text='No. of samples',font =fnt,bg ='LightSteelBlue2')
        Labelsample.grid(row=1,column=3,padx=5,pady=10)
        
        self.ParavalueentriesStart=[]
        self.ParavalueentriesEnd=[]
        self.ParavalueentriesSample=[]
        for i in range(self.ParameterCountUserInput):
            self.Numofparameters_parasweep = i+2
            Labeldesignparameter = tk.Label(self.root3, text=str(self.usergivenparanamessaved[i])+':',font =fnt,bg ='LightSteelBlue2')
            Labeldesignparameter.grid(row=self.Numofparameters_parasweep,column=0,padx=5,pady=10)
            self.startinputdesignparameter = tk.Entry(self.root3, width = 10)#width =200/100 for desktop/laptop
            self.startinputdesignparameter.grid(row=self.Numofparameters_parasweep,column=1,padx=5,pady=10)
            self.endinputdesignparameter = tk.Entry(self.root3, width = 10)#width =200/100 for desktop/laptop
            self.endinputdesignparameter.grid(row=self.Numofparameters_parasweep,column=2,padx=5,pady=10)
            self.sampleinputdesignparameter = tk.Entry(self.root3, width = 10)#width =200/100 for desktop/laptop
            self.sampleinputdesignparameter.grid(row=self.Numofparameters_parasweep,column=3,padx=5,pady=10)
            self.ParavalueentriesStart.append(self.startinputdesignparameter)
            self.ParavalueentriesEnd.append(self.endinputdesignparameter)
            self.ParavalueentriesSample.append(self.sampleinputdesignparameter)
        
        # LabelsweepparameterA = tk.Label(self.root3, text='a',font =("Helvetica",14),bg ='LightSteelBlue2')
        # LabelsweepparameterA.grid(row=self.row1,column=0,padx=5,pady=10)
        # self.startinputdesignparameterA = tk.Entry(self.root3, width = 10)#width =200/100 for desktop/laptop
        # self.startinputdesignparameterA.grid(row=self.row1,column=1,padx=5,pady=10)
        # self.endinputdesignparameterA = tk.Entry(self.root3, width = 10)#width =200/100 for desktop/laptop
        # self.endinputdesignparameterA.grid(row=self.row1,column=2,padx=5,pady=10)
        # self.sampleinputdesignparameterA = tk.Entry(self.root3, width = 10)#width =200/100 for desktop/laptop
        # self.sampleinputdesignparameterA.grid(row=self.row1,column=3,padx=5,pady=10)
        
        if self.value_inside_outputtype.get() == 'Gain' or self.value_inside_outputtype.get()== "Gain(f)" or self.value_inside_outputtype.get()=="Gain(\u03F4)": 
            Label_gain_loc = tk.Label(self.root3, text='Gain Location',font =("Courier Font",12),bg ='LightSteelBlue2')
            Label_gain_loc.grid(row=self.Numofparameters_parasweep+2,column=0)
            self.myspinbox_gain_loc = tk.Spinbox(self.root3,from_ =0,to=10,width=3,font =fnt)
            self.myspinbox_gain_loc.grid(row=self.Numofparameters_parasweep+2,column=1)
            
        calculateSweep_button = tk.Button(self.root3, text='Validate',command = self.update_sweepparameter_values,fg = 'white',bg ='DodgerBlue3')
        calculateSweep_button.grid(row=self.Numofparameters_parasweep+4,column=2)
            
        calculateSweep_button = tk.Button(self.root3, text='uploadfile',command = self.AskParaSweepFile,fg = 'white',bg ='DodgerBlue3')
        calculateSweep_button.grid(row=self.Numofparameters_parasweep+4,column=3)
        
        
        # Create the list of options
        self.options_list_parasweep = ["Linearly Spaced Values", "Random Values"]

        # Variable to keep track of the option
        # selected in OptionMenu
        self.value_inside_parasweep = tk.StringVar(self.root3)
        
        # Set the default value of the variable
        self.value_inside_parasweep.set("Select an Option")
        
        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.
        self.question_menu_parasweep = ttk.OptionMenu(self.root3, self.value_inside_parasweep, self.options_list_parasweep[0],*self.options_list_parasweep)
        self.question_menu_parasweep.grid(row=0,column=2,padx=5,pady=5)
        
        
        
        
        
        self.select_parasweep_option = tk.Label(self.root3, text ="Input type :",font =fnt,bg ='LightSteelBlue2')
        self.select_parasweep_option.grid(row=self.row6,column=1,padx=5,pady=5)
        
        self.Note = tk.Label(self.root3, text ="(Note: units should match training data units)",font =fnt,bg ='LightSteelBlue2')
        self.Note.place(x=40,y=320)
        
        
    def update_sweepparameter_values(self):
        self.usergivenparanames=[]
        for i in range(self.ParameterCountUserInput):
            self.usergivenparanames.append(str(self.usergivenparanamessaved[i]))
        print(self.usergivenparanames,'hi1')
        if self.value_inside_parasweep.get() == 'Linearly Spaced Values':
            for i in range(self.ParameterCountUserInput):
                self.usergivenparanames[i] = np.linspace(float(self.ParavalueentriesStart[i].get()),float(self.ParavalueentriesEnd[i].get()),int(self.ParavalueentriesSample[i].get()))
                
        elif self.value_inside_parasweep.get() == 'Random Values':
            
            for i in range(self.ParameterCountUserInput):
                self.tempx=[]
                for j in range(int(self.ParavalueentriesSample[i].get())):
                    self.temp = random.uniform(float(self.ParavalueentriesStart[i].get()),float(self.ParavalueentriesEnd[i].get()))
                    self.tempx.append(self.temp)
                self.usergivenparanames[i] = self.tempx   
            # self.A_values = []
            # self.B_values = []
            # self.D_values = []
            # self.N_values = []
            # for i in range(self.sampleA):
            #     self.tempA = random.uniform(self.startA,self.endA)
            #     self.A_values.append(self.tempA)
                
            #     self.tempB = random.uniform(self.startB,self.endB)
            #     self.B_values.append(self.tempB)
                
            #     self.tempD = random.uniform(self.startD,self.endD)
            #     self.D_values.append(self.tempD)
                
            #     self.tempN = random.uniform(self.startN,self.endN)
            #     self.N_values.append(self.tempN)
        
        self.dfa = pd.DataFrame()
        for i in range(self.ParameterCountUserInput):
            self.dfa.insert(loc=i, column=str(self.usergivenparanamessaved[i]), value=self.usergivenparanames[i])
            
      
        filename = "sweepparametervalues_samplesize"+str(self.ParavalueentriesSample[0].get())+".xlsx"
        self.datatoexcel = pd.ExcelWriter(filename)
        self.dfa.to_excel(self.datatoexcel,index=False)
        self.datatoexcel.save()
        if self.value_inside_outputtype.get() == 'Gain' or self.value_inside_outputtype.get()== "Gain(f)" or self.value_inside_outputtype.get()=="Gain(\u03F4)":
            self.ParaSweepGain(filename)
        elif self.value_inside_outputtype.get() == 'S11':
            self.ParaSweepS11(filename)
    def AskParaSweepFile(self):
        
        self.SweepFile = filedialog.askopenfilename(initialdir = "/Users/sinf5/Desktop/python", title ="select parametric sweep file", filetypes=[("Excel files", ".xlsx .xls")])
        if self.value_inside_outputtype.get() == 'Gain' or self.value_inside_outputtype.get()== "Gain(f)" or self.value_inside_outputtype.get()=="Gain(\u03F4)":
            self.ParaSweepGain(self.SweepFile)
        elif self.value_inside_outputtype.get() == 'S11':
            self.ParaSweepS11(self.SweepFile)
    def ParaSweepGain(self,path):
        count =0 
        self.gain_loc =int(self.myspinbox_gain_loc.get())
        self.Toutput = []
        self.name = "df_SweepValues" + str(self.ParavalueentriesSample[0].get())
        print(self.name,'hi')
        self.name = pd.DataFrame()
        self.name = pd.read_excel(path)
        self.dfa = pd.DataFrame()
        self.dfa = pd.read_excel(path)
        self.temp = self.name.values.tolist()
        filename = 'KNR'
        loaded_model = pickle.load(open(filename, 'rb'))
        for count in range(len(self.temp)):
            self.Toutput.append(loaded_model.predict([self.temp[count]]))
            print([self.temp[count]])
            count=count+1
        x = np.linspace(1,len(self.Toutput),len(self.Toutput))
        figure =plt.figure(figsize = (10,8),dpi =100)
        global df 
        df = pd.DataFrame()
        print(len(self.Toutput))
        for i in range(len(self.Toutput)):
            print(i)
            col = "prediction "+str(i+1)
            data = (self.Toutput[i].tolist())
            df.insert(loc = i, column= col, value= data[0])
        print(df)
        self.dfdel_global=pd.DataFrame(df.iloc[self.gain_loc,:])
        figure.add_subplot(111).plot(x, df.iloc[self.gain_loc,:])
        chart = FigureCanvasTkAgg(figure,self.root2)
        chart.get_tk_widget().place(x=600,y = 10)
        # naming the x axis
        plt.xlabel('Prediction input')
        # naming the y axis
        plt.ylabel('Gain (dBi)')
        # giving a title to my graph
        plt.title('ML Prediction')
     
        # show a legend on the plot
        plt.legend()
        self.var = 0
        for i in range(len(df.iloc[self.gain_loc,:])):
            
            if df.iloc[self.gain_loc,i]> self.var:
                self.var = df.iloc[self.gain_loc,i]
                self.loca = i
        print('Lookhere')
        print(self.temp[self.loca],self.var)
        self.parasweep_text.insert(tk.END, 'Maximum gain observed was '+ str(self.var)+ 'dBi for the input '+str(self.temp[self.loca]) +'\n')
                
    def ParaSweepS11(self,path):
        
       
        self.FMax = float(self.inputFMax.get())
        self.FMin = float(self.inputFMin.get())
        count =0 
        self.Toutput = []
        self.name = "df_SweepValues" + str(self.sampleinputdesignparameter)
        # print(self.name)
        self.name = pd.DataFrame()
        self.name = pd.read_excel(path)
        self.temp = self.name.values.tolist()
        filename = 'KNR'
        loaded_model = pickle.load(open(filename, 'rb'))
        for count in range(len(self.temp)):
            self.Toutput.append(loaded_model.predict([self.temp[count]]))
            # print([self.temp[count]])
            count=count+1
        
        x = np.linspace(1,len(self.Toutput),len(self.Toutput))
        figure =plt.figure(figsize = (10,8),dpi =100)
        global df 
        df = pd.DataFrame()
        # print(len(self.Toutput))
        for i in range(len(self.Toutput)):
            # print(i)
            col = "prediction "+str(i+1)
            data = (self.Toutput[i].tolist())
            df.insert(loc = i, column= col, value= data[0])
        self.diff=[]
        self.maxvar=0
        self.loca_s11=0
        self.BW = np.linspace(self.FMin,self.FMax,len(df.iloc[:,1]))
        # print(self.BW)
        # print(len(df.iloc[:,1]))
        # df.to_excel('Readme2.xlsx', index = False)
        for i in range(len(df.iloc[1,:])):
            data = []
            data = df.iloc[:,i].values.tolist()
            dat1 = np.array(data)
            count = 0
            start = 0
            end= 0
            for j in range(len(dat1)):
                if dat1[j] <-10 and count <1:
                    start = self.BW[j]
                    count = +1
                elif dat1[j] > -10 and count == 1:
                    end = self.BW[j-1]
                    count = +1
                    break
            if ((start == self.BW[0]) and (end ==0)):
                start = 0
                end = 0
            if (end-start)>self.maxvar:
                self.maxvar= abs(end-start)
                # print(self.maxvar)
                self.loca_s11 = i
            self.diff.append(abs(end-start))
        print(self.diff)
        self.dfdel_global=pd.DataFrame(self.diff)
        figure.add_subplot(111).plot(x, self.diff)
        chart = FigureCanvasTkAgg(figure,self.root2)
        chart.get_tk_widget().place(x=600,y = 10)
        # naming the x axis
        plt.xlabel('Prediction input')
        # naming the y axis
        plt.ylabel('Bandwidth (MHz)')
        # giving a title to my graph
        plt.title('ML Prediction')
     
        # show a legend on the plot
        plt.legend()
        self.parasweep_text.insert(tk.END, 'Maximum bandwidth observed was '+ str(self.maxvar)+ 'MHz for the input '+str(self.temp[self.loca_s11]) +'\n')        
    
    def update_parameter_values(self):
        self.usergivenparanames=[]
        for i in range(self.ParameterCountUserInput):
            self.usergivenparanames.append(str(self.usergivenparanamessaved[i]))
            self.usergivenparanames[i]=float(self.inputvalue[i].get())
        self.FMax = float(self.inputFMax.get())
        self.FMin = float(self.inputFMin.get())
        self.gettingdata()
    def Parameterinfo(ParameterCount,ParameterList):
        ParaCount =ParameterCount
        ParaList = ParameterList
        print(ParaCount,ParaList)
        for x in range(ParaCount):
            ParaList[x] = tk.Label(root,text = ParaList[x] + ':',font =fnt,bg ='LightSteelBlue2')
        
    def gettingdata(self):
        
        self.dfa = pd.DataFrame()
        ls =[]
        for i in range(self.ParameterCountUserInput):
            print(i,self.usergivenparanames[i])
            self.dfa.insert(loc=i, column=str(self.usergivenparanamessaved[i]), value=[self.usergivenparanames[i]])
            ls.append([self.usergivenparanames[i]])
        
        
        #loadingModel
        filename = 'KNR'
        loaded_model = pickle.load(open(filename, 'rb'))
        print(self.dfa)
        
        
        test_output = loaded_model.predict(self.dfa)
        self.dfdel_global = pd.DataFrame(test_output.T)
        print("lookhereyou",self.counter_1,test_output)

        
        filename = "Outputishere"+".xlsx"
        outputdatatoexcel = pd.ExcelWriter(filename)
        self.dfdel_global.to_excel(outputdatatoexcel,index=False)
        outputdatatoexcel.save()
        
        
        self.counter_1 = +1
        outputs.append(test_output)
        print(1)
        print(self.FMin)
        print(self.FMax)
        print(len(test_output[0]))
        x = np.linspace((self.FMin)/10e2,(self.FMax)/10e2,num=len(test_output[0]))
        # target = self.df_target
        # # plotting the line 1 points
        # plt.plot(x, target, label = "FEKO")
         
        # plotting the line 2 points
        test_output = test_output.T
        figure =plt.figure(figsize = (6,4),dpi =100)
        print(outputs)
        
        # dfdel = pd.DataFrame(outputs).T
        # dfdel.to_excel(excel_writer = "output_test.xlsx")
        # dfdel.to_excel('output_here.xlsx', index = False)
        for i in range(len(outputs)):
            ml = "Prediction "
            lab = ml + str(i+1)
            figure.add_subplot(111).plot(x, outputs[i].T, label = lab)
            
            chart = FigureCanvasTkAgg(figure,self.root2)
            chart.get_tk_widget().place(x=600,y = 10)
            # naming the x axis
            plt.xlabel('Theta (Degree)')
            # naming the y axis
            if self.value_inside_outputtype.get() == 'Gain' or self.value_inside_outputtype.get()== "Gain(f)" or self.value_inside_outputtype.get()=="Gain(\u03F4)":
                plt.ylabel('Gain (dBi)')
            elif self.value_inside_outputtype.get() == 'S11':
                plt.ylabel('S11 (dB)')
            
            # giving a title to my graph
            plt.title('ML Prediction')
            plt.grid()
            # show a legend on the plot
            plt.legend()
         
            # function to show the plot
       

       
    
       
    
      
    
validate_button = tk.Button(root, text='Validate',command = window2,fg = 'white',bg ='DodgerBlue3')#,
validate_button.place(x= 1100,y=300)


root.mainloop()