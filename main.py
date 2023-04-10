#########KM to MILE converter##########
from tkinter import *

#######Window config#######
window = Tk()
window.title('KM to Mile converter')
window.minsize(width=500, height=300)
window.config(bg='white', padx=50, pady=50)


###########Labels######################
title_label = Label(text='KM to Mile converter', font=("Arial", 16, "bold"), fg='navy', bg='SlateGray2')
title_label.grid(row=0, column=1)
title_label.config(padx=20, pady=30)

km_des_label = Label(text='Distance in kilometers:', font=("Arial", 12, "normal"), fg='navy', bg='white')
km_des_label.grid(row=1, column=0)
km_des_label.config(pady=20)

km_label = Label(text='Kilometers', font=("Arial", 12, "normal"), fg='navy', bg='white')
km_label.grid(row=1, column=2)
km_label.config(pady=20)


ml_des_label = Label(text='It is:', font=("Arial", 12, "normal"), fg='navy', bg='white')
ml_des_label.grid(row=2, column=0)
ml_des_label.config(pady=50)

ml_label = Label(text='Miles', font=("Arial", 12, "normal"), fg='navy', bg='white')
ml_label.grid(row=2, column=2)
ml_label.config(pady=50)

ml_result_label = Label(text='0', font=("Arial", 12, "normal"), fg='navy', bg='white')
ml_result_label.grid(row=2, column=1)
ml_result_label.config(pady=50)



########Entry config###########
entry = Entry(width=40)
entry.grid(row=1, column=1)


#########Button################

def km_to_mile():
    km = float(entry.get())
    result = round(km*0.621371192,2)
    ml_result_label.config(text=result, font=("Arial", 14, "normal"), fg='navy', bg='white')
    # print(ml_distance)

# km_to_mile(entry_input)
convert_button = Button(text="CALCULATE", command=km_to_mile)
convert_button.grid(row=3, column=1)
convert_button.config(padx=70, pady=5, bg='navy', fg='white',font=("Arial", 12, "bold"))



######Aplication loop#############
window.mainloop()