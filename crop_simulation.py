#SWITCHING LAYOUTS

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from radio_button_widget_class import *
from potato_class import *
from wheat_class import *
class CropWindow(QMainWindow):
    """Main Window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()
    def create_select_crop_layout(self):
        #intitial layout of the window-to select crop type

        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation","Please select a crop",("Wheat","Potato"))
        self.instantiate_button = QPushButton("Create Crop")

        #create layout
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_crop_widget)

        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)
    def create_view_crop_layout(self,crop_type):
        #this is the second layout window - view the crop growth
        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QlineEdit()
        self.status_line_edit = QLineEdit()

        self.manual_grow_button = QPushButton("Manually Grow")
        self.automatic_grow_button = QPushButton("Automatically Grow")

        self.grow_grid= QGridLayout()
        self.status_grid = QGridLayout()

        #Add  label widgets to the status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #Add line edit to the status layout
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit, 2,1)

        #add widgets/layouts to the grow layout
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        #create a widget to display the grow layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)


    
        
        
    

        
    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button() # get the radio button that was selected
        if crop_type == 1:
            self.simulated_crop = Wheat()
            
        elif crop_type == 2:
            self.simulated_crop = Potato()
        print(self.simulated_crop)

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec()

if __name__ == "__main__":
    main()
