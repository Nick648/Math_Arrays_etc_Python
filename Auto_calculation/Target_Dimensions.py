import sys
import math
import pyautogui as pg
from tkinter import *
from tkinter import ttk, messagebox

WIN_WIDTH, WIN_HEIGHT = pg.size()  # Get the size of the primary monitor.
APP_WIDTH, APP_HEIGHT = 600, 800
max_size_frame, min_size_element = 161, 3


def is_valid_digit(new_val: str) -> bool:
    if not new_val or new_val.isdigit() and len(new_val) < 5:
        return True
    else:
        return False


class TargetSizes:
    def __init__(self):
        # Main window
        self.root = Tk()
        self.set_configure()
        # CONST's
        self.target_frame, self.canvas_w, self.canvas_h = None, None, None
        self.input_width, self.input_height = [], []
        self.pos_width, self.pos_height = [], []
        self.canvas_elements = []
        # WIDGETS
        self.lbl_main = Label(master=self.root, text=f"The size of the target in centimeters",
                              font=('Ubuntu', 18, 'italic'), fg='#FFB841', bg="#79553D", padx=5, pady=3)
        self.lbl_size_input = Label(master=self.root, text="Element WIDTHxHEIGHT: ", font=('Ubuntu', 10),
                                    fg='#FFB02E', bg="#79553D", padx=5, pady=3)
        self.lbl_x_input = Label(master=self.root, text="x", font=('Ubuntu', 12), fg='#FFB02E', bg="#79553D")
        check_valid_digit = (self.root.register(is_valid_digit), "%P")
        self.entry_width_input = Entry(master=self.root, validate="key", validatecommand=check_valid_digit,
                                       font=('Times', 12,), width=5)
        self.entry_height_input = Entry(master=self.root, validate="key", validatecommand=check_valid_digit,
                                        font=('Times', 12,), width=5)
        self.btn_add_element = Button(master=self.root, text="Add", command=self.add_element, width=6)
        self.btn_delete_element = Button(master=self.root, text="Delete", command=self.delete_element, width=6)
        self.text_pos_elements = Text(master=self.root, wrap="word",
                                      font=('Ubuntu', 10), fg='#FFB02E', bg="#1E5945", padx=5, pady=3)
        self.text_pos_elements.insert(index=1.0, chars='Input sizes: ')
        self.text_pos_elements.configure(state='disabled')
        self.y_scroll = ttk.Scrollbar(orient="vertical", command=self.text_pos_elements.yview)
        self.text_pos_elements["yscrollcommand"] = self.y_scroll.set
        # RADIOBUTTON FOR INPUT
        self.selected_input = IntVar()
        self.selected_input.set(1)
        self.rad_element = Radiobutton(master=self.root, text='Element', value=1, variable=self.selected_input,
                                       font=2, activeforeground='#B00000', bg="#79553D", fg='#D5713F',
                                       command=self.set_element_input)
        self.rad_frame = Radiobutton(master=self.root, text='Frame', value=2, variable=self.selected_input,
                                     font=2, activeforeground='#B00000', bg="#79553D", fg='#D5713F',
                                     command=self.set_frame_input)
        self.lbl_selected_element = Label(master=self.root, text="The final Element WIDTHxHEIGHT: ",
                                          font=('Ubuntu', 10), fg='#FFB02E', bg="#79553D", padx=5, pady=3)
        self.width_selected_element, self.height_selected_element = IntVar(), IntVar()
        self.cmbx_width_selected_element = ttk.Combobox(master=self.root, textvariable=self.width_selected_element,
                                                        values=[], width=5)
        self.lbl_x_selected_element = Label(master=self.root, text="x", font=('Ubuntu', 12), fg='#FFB02E', bg="#79553D")
        self.cmbx_height_selected_element = ttk.Combobox(master=self.root, textvariable=self.height_selected_element,
                                                         values=[], width=5)
        self.lbl_selected_frame = Label(master=self.root, text="The final Frame WIDTHxHEIGHT: ", font=('Ubuntu', 10),
                                        fg='#FFB02E', bg="#79553D", padx=5, pady=3)
        self.width_selected_frame, self.height_selected_frame = IntVar(), IntVar()
        self.cmbx_width_selected_frame = ttk.Combobox(master=self.root, textvariable=self.width_selected_frame,
                                                      values=[], width=5)
        self.lbl_x_selected_frame = Label(master=self.root, text="x", font=('Ubuntu', 12), fg='#FFB02E', bg="#79553D")
        self.cmbx_height_selected_frame = ttk.Combobox(master=self.root, textvariable=self.height_selected_frame,
                                                       values=[], width=5)
        self.lbl_depth_proposed = Label(master=self.root, text="Depth (cm): ", font=('Ubuntu', 10),
                                        fg='#FFB02E', bg="#79553D", padx=5, pady=3)
        self.entry_depth_input = Entry(master=self.root, validate="key", validatecommand=check_valid_digit,
                                       font=('Times', 12,), width=4)
        self.btn_calculate = Button(master=self.root, text="Calculate", width=9, command=self.calculate)
        self.result_text = Text(master=self.root, wrap="word", state='disabled',
                                font=('Ubuntu', 12), fg='#A5260A', bg="#FDD9B5", padx=5, pady=3)
        self.canvas = Canvas(self.root, bg='#2C3337', cursor='crosshair', width=500, height=400, highlightthickness=0)
        self.place_widgets()
        # Start display app
        self.root.mainloop()

    def set_configure(self) -> None:
        self.root.resizable(width=False, height=False)
        offset_width, offset_height = WIN_WIDTH // 2 - APP_WIDTH // 2, WIN_HEIGHT // 2 - APP_HEIGHT // 2
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{offset_width}+{offset_height}")
        self.root.configure(background="#79553D")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title('Target Dimensions')

    def place_widgets(self) -> None:
        self.lbl_main.place(relx=0.5, rely=0.01, anchor=N)
        self.lbl_size_input.place(relx=0.01, rely=0.07, anchor=NW)
        self.entry_width_input.place(relx=0.28, rely=0.07, anchor=NW)
        self.lbl_x_input.place(relx=0.361, rely=0.07, anchor=NW)
        self.entry_height_input.place(relx=0.39, rely=0.07, anchor=NW)
        self.btn_add_element.place(relx=0.52, rely=0.07, anchor=N)
        self.btn_delete_element.place(relx=0.62, rely=0.07, anchor=N)
        self.rad_element.place(relx=0.7, rely=0.07, anchor=NW)
        self.rad_frame.place(relx=0.85, rely=0.07, anchor=NW)
        self.text_pos_elements.place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.06, anchor=NW)
        self.y_scroll.place(relx=0.96, rely=0.19, relheight=0.08, anchor=SW)
        self.lbl_selected_element.place(relx=0.02, rely=0.2, anchor=NW)
        self.cmbx_width_selected_element.place(relx=0.39, rely=0.2, anchor=NW)
        self.lbl_x_selected_element.place(relx=0.484, rely=0.2, anchor=NW)
        self.cmbx_height_selected_element.place(relx=0.51, rely=0.2, anchor=NW)
        self.lbl_depth_proposed.place(relx=0.64, rely=0.2, anchor=NW)
        self.entry_depth_input.place(relx=0.78, rely=0.2, anchor=NW)
        self.lbl_selected_frame.place(relx=0.02, rely=0.25, anchor=NW)
        self.cmbx_width_selected_frame.place(relx=0.37, rely=0.25, anchor=NW)
        self.lbl_x_selected_frame.place(relx=0.464, rely=0.25, anchor=NW)
        self.cmbx_height_selected_frame.place(relx=0.491, rely=0.25, anchor=NW)
        self.btn_calculate.place(relx=0.85, rely=0.25, relheight=0.04, anchor=NW)
        self.result_text.place(rely=0.81, relx=0.5, relwidth=0.95, relheight=0.18, anchor=N)

    def zeroing_out(self):
        self.input_width, self.input_height, self.pos_width, self.pos_height = [], [], [], []
        self.entry_width_input.delete(0, END)
        self.entry_height_input.delete(0, END)
        self.text_pos_elements.configure(state='normal')
        self.text_pos_elements.delete(0.0, END)
        self.text_pos_elements.insert(index=1.0, chars='Input sizes: ')
        self.text_pos_elements.configure(state='disabled')
        self.cmbx_width_selected_element.configure(values=[])
        self.cmbx_height_selected_element.configure(values=[])
        self.width_selected_element.set(0)
        self.height_selected_element.set(0)
        self.cmbx_width_selected_frame.configure(values=[])
        self.cmbx_height_selected_frame.configure(values=[])
        self.width_selected_frame.set(0)
        self.height_selected_frame.set(0)
        self.result_text.configure(state='normal')
        self.result_text.delete(0.0, END)
        self.result_text.configure(state='disabled')

    def set_element_input(self):
        self.lbl_size_input.configure(text="Element WIDTHxHEIGHT: ")
        self.zeroing_out()

    def set_frame_input(self):
        self.lbl_size_input.configure(text="Frame WIDTHxHEIGHT: ")
        self.zeroing_out()

    def add_element(self):
        width, height = int(self.entry_width_input.get()), int(self.entry_height_input.get())
        finder = self.text_pos_elements.search(f'({width}x{height}); ', 0.0)
        if width and height and not finder:
            self.text_pos_elements.configure(state='normal')
            self.text_pos_elements.insert(index=END, chars=f'({width}x{height}); ')
            self.text_pos_elements.configure(state='disabled')
            self.input_width.append(int(width))
            self.input_width.sort()
            self.input_height.append(int(height))
            self.input_height.sort()
        self.change_possible_sizes()

    def delete_element(self):
        width, height = int(self.entry_width_input.get()), int(self.entry_height_input.get())
        finder = self.text_pos_elements.search(f'({width}x{height}); ', 0.0)
        if width and height and finder:
            row, pos = map(int, finder.split('.'))
            index_1, index_2 = float(f'{row}.{pos}'), float(f"{row}.{pos + len(f'({width}x{height}); ')}")
            self.text_pos_elements.configure(state='normal')
            self.text_pos_elements.delete(index_1, index_2)
            self.text_pos_elements.configure(state='disabled')
            self.input_width.pop(self.input_width.index(width))
            self.input_height.pop(self.input_height.index(height))
            self.change_possible_sizes()
        else:
            messagebox.showwarning(title="Warning", message="There is no data entered with such dimensions!")

    def change_possible_sizes(self):
        if self.selected_input.get() == 1:
            self.pos_width = get_nok_n(self.input_width)
            self.pos_height = get_nok_n(self.input_height)
            res_text = f"Possible size of frame: \n" \
                       f"\tWidth: {self.pos_width}\n" \
                       f"\tHeight: {self.pos_height}\n"
            self.cmbx_width_selected_element.configure(values=self.input_width)
            self.cmbx_height_selected_element.configure(values=self.input_height)
            self.cmbx_width_selected_frame.configure(values=self.pos_width)
            self.cmbx_height_selected_frame.configure(values=self.pos_height)
        elif self.selected_input.get() == 2:
            self.pos_width = get_nod_n(self.input_width)
            self.pos_height = get_nod_n(self.input_height)
            res_text = f"Possible size of elements: \n" \
                       f"\tWidth: {self.pos_width}\n" \
                       f"\tHeight: {self.pos_height}\n"
            self.cmbx_width_selected_frame.configure(values=self.input_width)
            self.cmbx_height_selected_frame.configure(values=self.input_height)
            self.cmbx_width_selected_element.configure(values=self.pos_width)
            self.cmbx_height_selected_element.configure(values=self.pos_height)
        else:
            res_text = '!'
        self.result_text.configure(state='normal')
        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, res_text)
        self.result_text.configure(state='disabled')
        self.entry_width_input.delete(0, END)
        self.entry_height_input.delete(0, END)
        self.width_selected_element.set(0)
        self.height_selected_element.set(0)
        self.width_selected_frame.set(0)
        self.height_selected_frame.set(0)

    def calculate(self):
        width_element, height_element = self.width_selected_element.get(), self.height_selected_element.get()
        width_frame, height_frame = self.width_selected_frame.get(), self.height_selected_frame.get()
        depth = self.entry_depth_input.get()
        if not width_element or not height_element:
            messagebox.showerror(title="Error", message="You need to select the dimensions of the element!")
        elif not width_frame or not height_frame:
            messagebox.showerror(title="Error", message="You need to select the dimensions of the frame!")
        elif not depth:
            messagebox.showerror(title="Error", message="You need to enter the depth in cm!")
        else:
            depth = int(depth)
            count_width = int(width_frame / width_element)
            count_height = int(height_frame / height_element)
            all_count_element = count_width * count_height
            necessary_length = all_count_element * depth
            max_length = max(width_element, height_element)
            log_diameter = math.ceil(math.sqrt(max_length ** 2 + max_length ** 2))
            res_text = f"Target characteristics: \n" \
                       f"    Count width elements = {count_width}\n" \
                       f"    Count height elements = {count_height}\n" \
                       f"    All count elements = {all_count_element}\n" \
                       f"    The total length of the bar = {necessary_length} cm\n" \
                       f"    Minimum diameter of the log = {log_diameter} cm"
            self.result_text.configure(state='normal')
            self.result_text.delete(0.0, END)
            self.result_text.insert(0.0, res_text)
            self.result_text.configure(state='disabled')
            self.draw_target_frame(width_frame=width_frame, height_frame=height_frame, width_element=width_element,
                                   height_element=height_element, count_width=count_width, count_height=count_height)

    def draw_target_frame(self, width_frame: int, height_frame: int, width_element: int, height_element: int,
                          count_width: int, count_height: int):
        self.canvas.place(relx=0.5, rely=0.3, anchor=N)
        if self.target_frame:
            self.canvas.delete(self.target_frame)
            self.canvas.delete(self.canvas_w)
            self.canvas.delete(self.canvas_h)
            for el in self.canvas_elements:
                self.canvas.delete(el)
            self.canvas_elements = []
        ideal_width, ideal_height = 200, 300
        final_width = get_nearest_digit(ideal_width, count_width)
        final_height = get_nearest_digit(ideal_height, count_height)
        offset_x, offset_y = final_width // count_width, final_height // count_height
        self.root.update()
        begin_x = self.canvas.winfo_width() / 2 - final_width / 2
        begin_y = self.canvas.winfo_height() / 2 - final_height / 2
        width_text, height_text = min(width_frame, height_frame), max(width_frame, height_frame)
        self.target_frame = self.canvas.create_rectangle(begin_x, begin_y, begin_x + final_width,
                                                         begin_y + final_height, width=2, outline="white")
        self.canvas_w = self.canvas.create_text(250, 25, anchor=N, text=f'{width_text}', fill="white", font="Arial 14")
        self.canvas_h = self.canvas.create_text(360, 200, anchor=NW, text=f'{height_text}', fill="white",
                                                font="Arial 14")
        for i in range(count_width):
            for j in range(count_height):
                begin_el_x, begin_el_y = begin_x + offset_x * i, begin_y + offset_y * j
                el = self.canvas.create_rectangle(begin_el_x, begin_el_y, begin_el_x + offset_x, begin_el_y + offset_y,
                                                  outline="blue", activedash=(5, 4))
                self.canvas_elements.append(el)

    def on_closing(self) -> None:
        self.root.destroy()
        sys.exit()


def get_nearest_digit(initial_dig: int, divider: int) -> int:
    if initial_dig % divider == 0:
        return initial_dig
    less_dig, more_dig = 0, 0
    for i in range(initial_dig - 100, initial_dig):
        if i % divider == 0:
            less_dig = i
    for i in range(initial_dig + 100, initial_dig, -1):
        if i % divider == 0:
            more_dig = i
    if abs(initial_dig - less_dig) < abs(initial_dig - more_dig):
        return less_dig
    else:
        return more_dig


def get_nod(a: int, b: int):
    math.gcd(a, b)


def get_nok_n(digs: list) -> list:
    if not digs:
        return []
    ans = []
    for i in range(max(digs), max_size_frame):
        k = True
        for dig in digs:
            if i % dig != 0:
                k = False
                break
        if k:
            ans.append(i)
    return ans


def get_nod_n(digs: list) -> list:
    if not digs:
        return []
    ans = []
    for i in range(min_size_element, min(digs)):
        k = True
        for dig in digs:
            if dig % i != 0:
                k = False
                break
        if k:
            ans.append(i)
    return ans


def main():
    app = TargetSizes()


if __name__ == '__main__':
    main()
