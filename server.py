""" Programda işlev yükleyebileceğiniz üç buton iki checkbox mevcut.
Tıklama ya da seçme eventlerinin bağlı olduğu fonksiyonlar yani dolduracağınız
kısımlar ellili satırlarda. İçerisine anlaşılması için yapılan işleme göre
print ifadeleri koydum. Kolay gelsin. """
from PyQt5 import QtCore, QtGui, QtWidgets
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 34469
flag = 255  # Protocol flag
s.bind((host, port))
s.listen()
print("Socket is listening...")
c, addr = s.accept()
print("Connected by", addr)


def send_data(data):
    sent = False
    global s
    global c
    global addr
    while not sent:
        try:
            c.sendall(data)
        except socket.error or socket.gaierror or socket.herror:
            print("Data was not sent, trying again...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            print("Socket is listening...")
            s.listen()
            c, addr = s.accept()
            print("Connected by", addr)
            continue
        break
    print("Sent data:", data)


class Ui_sample_ui(object):
    def setupUi(self, sample_ui):
        sample_ui.setObjectName("sample_ui")
        sample_ui.resize(250, 160)
        sample_ui.setMaximumSize(QtCore.QSize(500, 320))
        self.centralwidget_vl = QtWidgets.QWidget(sample_ui)
        self.centralwidget_vl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget_vl.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget_vl.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget_vl.setObjectName("centralwidget_vl")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget_vl)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_gl = QtWidgets.QGridLayout()
        self.main_gl.setObjectName("main_gl")
        self.checkbox_1_cb = QtWidgets.QCheckBox(self.centralwidget_vl)
        self.checkbox_1_cb.setObjectName("checkbox_1_cb")
        self.main_gl.addWidget(self.checkbox_1_cb, 3, 0, 1, 1)
        self.checkbox_1_cb.stateChanged.connect(lambda: self.f_checkbox_1_cb(self.checkbox_1_cb))
        self.checkbox_2_cb = QtWidgets.QCheckBox(self.centralwidget_vl)
        self.checkbox_2_cb.setObjectName("checkbox_2_cb")
        self.main_gl.addWidget(self.checkbox_2_cb, 3, 1, 1, 1)
        self.checkbox_2_cb.stateChanged.connect(lambda: self.f_checkbox_2_cb(self.checkbox_2_cb))
        self.buton_1_pb = QtWidgets.QPushButton(self.centralwidget_vl)
        self.buton_1_pb.setEnabled(True)
        self.buton_1_pb.setObjectName("buton_1_pb")
        self.main_gl.addWidget(self.buton_1_pb, 0, 0, 1, 2)
        self.buton_1_pb.clicked.connect(self.f_buton_1)
        self.buton_2_pb = QtWidgets.QPushButton(self.centralwidget_vl)
        self.buton_2_pb.setObjectName("buton_2_pb")
        self.main_gl.addWidget(self.buton_2_pb, 1, 0, 1, 2)
        self.buton_2_pb.clicked.connect(self.f_buton_2)
        self.buton_3_pb = QtWidgets.QPushButton(self.centralwidget_vl)
        self.buton_3_pb.setObjectName("buton_3_pb")
        self.main_gl.addWidget(self.buton_3_pb, 2, 0, 1, 2)
        self.buton_3_pb.clicked.connect(self.f_buton_3)
        self.verticalLayout.addLayout(self.main_gl)
        sample_ui.setCentralWidget(self.centralwidget_vl)
        self.retranslateUi(sample_ui)
        QtCore.QMetaObject.connectSlotsByName(sample_ui)

    def retranslateUi(self, sample_ui):
        _translate = QtCore.QCoreApplication.translate
        sample_ui.setWindowTitle(_translate("sample_ui", "sample_ui"))
        self.checkbox_1_cb.setText(_translate("sample_ui", "checkbox_1"))
        self.checkbox_2_cb.setText(_translate("sample_ui", "checkbox_2"))
        self.buton_1_pb.setText(_translate("sample_ui", "buton_1"))
        self.buton_2_pb.setText(_translate("sample_ui", "buton_2"))
        self.buton_3_pb.setText(_translate("sample_ui", "buton_3"))

    def f_buton_1(self):
        print("buton 1'e basıldı.")

        data1 = bytearray()
        data1.append(flag)
        data1.append(1)  # Function
        data1.append(45)  # Degree
        flag_sum = data1[1] + data1[2]
        print(flag_sum)
        data1.append(flag_sum)  # End flag

        send_data(data1)

    def f_buton_2(self):
        print("buton 2'ye basıldı.")

        data2 = bytearray()
        data2.append(flag)
        data2.append(2)  # Function
        data2.append(45)  # Degree
        flag_sum = data2[1] + data2[2]
        print(flag_sum)
        data2.append(flag_sum)  # End flag

        send_data(data2)

    def f_buton_3(self):
        print("buton 3'e basıldı.")

        data3 = bytearray()
        data3.append(flag)
        data3.append(3)  # Function
        data3.append(0)  # Redundant
        flag_sum = data3[1] + data3[2]
        print(flag_sum)
        data3.append(flag_sum)  # End flag

        send_data(data3)

    def f_checkbox_1_cb(self, checkbox_1_cb):
        if checkbox_1_cb.isChecked():
            print("checkbox 1 işaretlendi.")

            data4 = bytearray()
            data4.append(flag)
            data4.append(4)  # Function
            data4.append(1)  # ON
            flag_sum = data4[1] + data4[2]
            print(flag_sum)
            data4.append(flag_sum)  # End flag

            send_data(data4)

        elif not checkbox_1_cb.isChecked():
            print("checkbox 1'in işareti kaldırıldı.")

            data4 = bytearray()
            data4.append(flag)
            data4.append(4)  # Function
            data4.append(0)  # OFF
            flag_sum = data4[1] + data4[2]
            print(flag_sum)
            data4.append(flag_sum)  # End flag

            send_data(data4)

        else:
            pass

    def f_checkbox_2_cb(self, checkbox_2_cb):
        if checkbox_2_cb.isChecked():
            print("checkbox 2 işaretlendi.")

            data5 = bytearray()
            data5.append(flag)
            data5.append(5)  # Function
            data5.append(1)  # ON
            flag_sum = data5[1] + data5[2]
            print(flag_sum)
            data5.append(flag_sum)  # End flag

            send_data(data5)

        elif not checkbox_2_cb.isChecked():
            print("checkbox 2'in işareti kaldırıldı.")

            data5 = bytearray()
            data5.append(flag)
            data5.append(5)  # Function
            data5.append(0)  # OFF
            flag_sum = data5[1] + data5[2]
            print(flag_sum)
            data5.append(flag_sum)  # End flag

            send_data(data5)

        else:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    sample_ui = QtWidgets.QMainWindow()
    ui = Ui_sample_ui()
    ui.setupUi(sample_ui)
    sample_ui.show()
    sys.exit(app.exec_())

s.close()
