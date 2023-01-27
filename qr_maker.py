import qrcode
import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog

#QR Code maker and reader

class Main():

    def __init__(self,master):
        master.geometry("800x600")
        master.title("QR code maker and reader")
        master.resizable(False,False)
        self.font = (None,24)
        self.tab_control = ttk.Notebook(master)
        
        self.make_qr_code_tab = tk.Frame(self.tab_control)
        self.tab_control.add(self.make_qr_code_tab,text="Make QR code")
        
        self.read_qr_code_tab = tk.Frame(self.tab_control)
        self.tab_control.add(self.read_qr_code_tab,text="Read QR code")
        
        self.tab_control.pack(expand=1,fill="both")

        #MAKE QR CODE TAB CONTENT
        self.valueLabel = tk.Label(self.make_qr_code_tab,text="Value : ",font=self.font)
        self.valueLabel.grid(row=0,column=0)

        self.ValueEntry = tk.Entry(self.make_qr_code_tab,font=self.font)
        self.ValueEntry.grid(row=0,column=1)

        self.clear_button = tk.Button(self.make_qr_code_tab,command=self.clear_ValueEntry,text="CLEAR",font=self.font)
        self.clear_button.grid(row=0,column=2)
        
        self.create_qr_code_button = tk.Button(self.make_qr_code_tab,command=self.create_qr_code,text="CREATE",font=self.font)
        self.create_qr_code_button.grid(row=1,columnspan=5,padx=300,pady=150)

        #READ QR CODE CONTENT
        self.filename = tk.Entry(self.read_qr_code_tab,font=self.font,state="disabled")
        self.filename.grid(row= 0,columnspan=5)

        self.open_file_button = tk.Button(self.read_qr_code_tab,command=self.read_qr_code,text="OPEN FILE",font=self.font)
        self.open_file_button.grid(row=0,column=6)

        self.qr_code_content_label = tk.Label(self.read_qr_code_tab,text="QR CODE CONTENT",font=self.font)
        self.qr_code_content_label.grid(row=1,column=0,padx=10,pady=10)
        self.qr_code_content = tk.Text(self.read_qr_code_tab,state="disable",font=(None,20),width=35,height=12)
        self.qr_code_content_scroll_bar = tk.Scrollbar(self.read_qr_code_tab,command=self.qr_code_content.yview)
        self.qr_code_content.configure(yscrollcommand=self.qr_code_content_scroll_bar.set)
        self.qr_code_content.grid(rowspan=5,columnspan=10)
        self.qr_code_content_scroll_bar.grid(row=2,column=11)
    def create_qr_code(self):
        self.filename = None
        try:
            self.filename = filedialog.asksaveasfilename(defaultextension= "*.jpg",
                                                                              filetypes=[("jpg file", "*.jpg"),
                                                                                              ("jpeg file", "*.jpeg"),
                                                                                              ("png file", "*.png")])
            image = qrcode.make(self.ValueEntry.get())
            image.save(self.filename)
        except Exception as e:
            msg.showwarning(title="WARNING",message=e)

    def clear_ValueEntry(self):
        self.ValueEntry.delete(0,tk.END)

    def read_qr_code(self):
        self.filename = None
        try:
            self.filename = filedialog.askopenfilename(defaultextension="*.jpg",
                                                                            filetypes=[("jpg file","*.jpg"),
                                                                                            ("png file","*.png"),
                                                                                             ("jpeg file","*.jpeg")])

            qrcode = cv2.QRCodeDetector()
            val,a,b = qrcode.detectAndDecode(cv2.imread(self.filename))
            self.qr_code_content.configure(state="normal")
            self.qr_code_content.delete(1.0,tk.END)
            self.qr_code_content.insert(1.0,val)
            self.qr_code_content.configure(state="disabled")
        except Exception as e:
            msg.showwarning(title="WARNING",message=e)
            

if __name__ == "__main__":
    master = tk.Tk()
    main = Main(master)
    master.mainloop()
    
