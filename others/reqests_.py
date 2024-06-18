from requests import *
from tkinter import *
from pygal import *
def todo_diagram():
    diagro=Bar()
    diagro.title="git hub most popular guys in python sphere"
    diagro.x_labels=name_guy
    diagro.add("",stargazer_guy)
    diagro.render_in_browser()
def open_guyinfo(event):
    nwin=Toplevel()
    nwin.title("Github guy")
    nwin.geometry("1400x400")
    nwin['bg'] = 'orange'
    main_dict=r_list[int(*lb.curselection())]
    inflbl=Label(master=nwin, bg='orange',font=14, text=f"name:{lb.get(lb.curselection())}\ndescription:{main_dict['description']}\nstargazers:{main_dict['stargazers_count']}")
    textbox=Text(master=nwin, width=50, height=2)
    textbox.insert(1.0, main_dict['html_url'])
    inflbl.pack()
    textbox.pack()
root=Tk()
root.title("Github guys")
root.geometry("300x400")
root['bg']='orange'
URL_site="https://api.github.com/search/repositories?q=python{&page,per_page,sort,order}&sort:stars"
r=get(URL_site)
r_dict=r.json()
r_list=r_dict['items']
name_guy=[]
stargazer_guy=[]
lb=Listbox()
for i in range(10):
    lb.insert(i, r_list[i]['name'])
    name_guy.append(r_list[i]['name'])
    stargazer_guy.append(r_list[i]['stargazers_count'])
lb.pack()
lb.bind("<Double-Button-1>", open_guyinfo)
btn=Button(bg='grey', text="Create Diogram",command=todo_diagram)
btn.pack()
mainloop()