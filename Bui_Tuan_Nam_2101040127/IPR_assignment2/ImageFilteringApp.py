import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QComboBox, QHBoxLayout, QSlider, QSizePolicy
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtCore import Qt
import cv2
import numpy as np

class ImageFilteringApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fourier Transform Image Filtering")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(400, 400)
        self.image_label.setStyleSheet("border: 2px solid black; background-color: #f0f0f0;")

        self.load_button = QPushButton("Upload Image")
        self.load_button.clicked.connect(self.load_image)
        self.load_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.filter_label = QLabel("Select Filter:")
        self.filter_label.setAlignment(Qt.AlignLeft)
        self.filter_label.setStyleSheet("font-weight: bold;")

        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Default", "Low Pass", "High Pass", "Band Pass" ])
        self.filter_combo.setCurrentIndex(0)  # Giữ mặc định là "None"
        self.filter_combo.currentIndexChanged.connect(self.apply_filter)
        self.filter_combo.setStyleSheet("padding: 5px;")

        self.slider_label = QLabel("Filter Strength:")
        self.slider_label.setAlignment(Qt.AlignCenter)
        self.slider_label.setStyleSheet("font-weight: bold;")

        self.filter_slider = QSlider(Qt.Horizontal)
        self.filter_slider.setMinimum(1)
        self.filter_slider.setMaximum(100)
        self.filter_slider.setValue(50)
        self.filter_slider.setTickInterval(10)
        self.filter_slider.setTickPosition(QSlider.TicksBelow)
        self.filter_slider.valueChanged.connect(self.apply_filter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.load_button, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.filter_label)
        self.layout.addWidget(self.filter_combo)
        self.layout.addWidget(self.slider_label)
        self.layout.addWidget(self.filter_slider)
        self.layout.setContentsMargins(20, 20, 20, 20)

        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addStretch()  # Thêm stretch để căn lề vào giữa cửa sổ
        central_layout.addLayout(self.layout)
        central_layout.addStretch()  # Thêm stretch để căn lề vào giữa cửa sổ
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        self.loaded_image = None
        self.filtered_image = None

    def load_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.loaded_image = cv2.imread(file_path)
            self.display_image(self.loaded_image)

    def display_image(self, image):
        if image is None:
            return
        if len(image.shape) == 3:
            h, w, _ = image.shape
            bytes_per_line = 3 * w
            qt_image = QPixmap.fromImage(QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped())
            self.image_label.setPixmap(qt_image)
        else:
            h, w = image.shape
            qt_image = QPixmap.fromImage(QImage(image.data, w, h, w, QImage.Format_Grayscale8))
            self.image_label.setPixmap(qt_image)

    def apply_filter(self):
        if self.loaded_image is None:
            return
        filter_type = self.filter_combo.currentText()
        if filter_type == "Default":
            self.display_image(self.loaded_image) 
            return

        gray_image = cv2.cvtColor(self.loaded_image, cv2.COLOR_BGR2GRAY)
        gray_image = gray_image.astype(np.float32) / 255.0

        dft = cv2.dft(gray_image, flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)

        rows, cols = gray_image.shape
        crow, ccol = rows // 2, cols // 2

        if filter_type == "Low Pass":
            r = self.filter_slider.value() * 2
            mask = np.zeros((rows, cols, 2), np.float32)
            mask[crow - r:crow + r, ccol - r:ccol + r] = 1

        elif filter_type == "High Pass":
            r = self.filter_slider.value() * 2
            mask = np.ones((rows, cols, 2), np.float32)
            mask[crow - r:crow + r, ccol - r:ccol + r] = 0

        elif filter_type == "Band Pass":
            low_cutoff = 0.1 * self.filter_slider.value()
            high_cutoff = 0.3 * self.filter_slider.value()
            mask = np.zeros((rows, cols, 2), np.float32)
            mask[int(crow - high_cutoff):int(crow + high_cutoff), int(ccol - high_cutoff):int(ccol + high_cutoff)] = 1
            mask[int(crow - low_cutoff):int(crow + low_cutoff), int(ccol - low_cutoff):int(ccol + low_cutoff)] = 0

        dft_shift_filtered = dft_shift * mask

        filtered_image = cv2.idft(np.fft.ifftshift(dft_shift_filtered))
        filtered_image = cv2.magnitude(filtered_image[:, :, 0], filtered_image[:, :, 1])

        filtered_image = cv2.normalize(filtered_image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        self.filtered_image = (filtered_image * 255).astype(np.uint8)

        self.display_image(self.filtered_image)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFilteringApp()
    window.show()
    sys.exit(app.exec_())
