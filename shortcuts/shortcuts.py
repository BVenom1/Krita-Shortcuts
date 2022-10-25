from krita import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

# class for dialog box to display shortcuts
class ShortcutDialog(QWidget):
    def __init__(self):
        super().__init__(None, Qt.Window | Qt.FramelessWindowHint)
        self.setLayout(QFormLayout())
        label = QLabel('Test Label')
        self.layout().addRow(label)
        
    def keyReleaseEvent(self, keyEvent):
        if keyEvent.isAutoRepeat() == False:
            self.setVisible(False)

# class for shortcuts menu
class Shortcuts(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    # Krita.instance() exists, so do any setup work
    def setup(self):

        # make a debug dialog box
        self.debugDialog = ShortcutDialog()

        Krita.instance().notifier().windowCreated.connect(self.on_windowCreated)
        
    # called after setup(self)
    def createActions(self, window):
        self.exampleShortcut = QAction('Example Shortcut')
        self.exampleShortcut.setShortcut('Ctrl+J')
        self.exampleShortcut.setStatusTip('A Simple Test')
        self.exampleShortcut.triggered.connect(self.on_exampleShortcut)
    
    # function called when custom shortcut is clicked
    def on_exampleShortcut(self):
        if self.debugDialog.isVisible() == False:
            self.debugDialog.setVisible(True)

    # Function is called when window is fully created, adds menu to the menu bar
    def on_windowCreated(self):
        
        # add menu to menu bar
        menuBar = Krita.instance().activeWindow().qwindow().menuBar()
        self.menu = menuBar.addMenu('Shortcuts')

        # add shortcuts to menu
        self.menu.addAction(self.exampleShortcut)
    
    # generic popup message function
    def popup(self, string: str):
        QMessageBox.information(QWidget(), 'Grid Splitter', string)

    # function to make a debug message popup
    def debugPopup(self):
        self.popup('debug')
