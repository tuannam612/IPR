import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QComboBox, QHBoxLayout, QSlider, QSizePolicy
from PyQt5.QtGui import QPixmap, QImage, QFont, QColor
from PyQt5.QtCore import Qt
import cv2
import numpy as np

class ImageFilteringApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fourier Transform Image Filtering")
        self.setGeometry(100, 100, 800, 600)

        # Create a large title label
        self.title_label = QLabel("Fourier Transform", self)
        title_font = QFont("Arial", 24, QFont.Bold)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: blue;")  # Set title label color

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(400, 400)
        self.image_label.setStyleSheet("border: 2px solid black; background-color: #f0f0f0;")

        self.size_label = QLabel()  # Label to display original image size
        self.size_label.setAlignment(Qt.AlignCenter)

        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)
        self.load_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.load_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px 24px; text-align: center; font-size: 16px; margin: 4px 2px")

        self.filter_label = QLabel("Select Filter:")
        self.filter_label.setAlignment(Qt.AlignLeft)
        self.filter_label.setStyleSheet("font-weight: bold; color: red;")

        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Default", "Low Pass", "High Pass", "Band Pass"])
        self.filter_combo.setCurrentIndex(0)
        self.filter_combo.currentIndexChanged.connect(self.apply_filter)
        self.filter_combo.setStyleSheet("padding: 5px; background-color: #f0f0f0; color: black;")

        self.slider_label = QLabel("Filter Strength:")
        self.slider_label.setAlignment(Qt.AlignCenter)
        self.slider_label.setStyleSheet("font-weight: bold; color: green;")

        self.filter_slider = QSlider(Qt.Horizontal)
        self.filter_slider.setMinimum(1)
        self.filter_slider.setMaximum(100)
        self.filter_slider.setValue(50)
        self.filter_slider.setTickInterval(10)
        self.filter_slider.setTickPosition(QSlider.TicksBelow)
        self.filter_slider.valueChanged.connect(self.apply_filter)

        self.resize_label = QLabel("Resize Image:")
        self.resize_label.setAlignment(Qt.AlignLeft)
        self.resize_label.setStyleSheet("font-weight: bold; color: orange;")

        self.resize_slider = QSlider(Qt.Horizontal)
        self.resize_slider.setMinimum(10)
        self.resize_slider.setMaximum(200)
        self.resize_slider.setValue(100)
        self.resize_slider.setTickInterval(10)
        self.resize_slider.setTickPosition(QSlider.TicksBelow)
        self.resize_slider.valueChanged.connect(self.resize_image)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label, alignment=Qt.AlignCenter)  # Add the title label to the layout
        self.layout.addWidget(self.load_button, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.size_label, alignment=Qt.AlignCenter)  # Add size label to the layout
        self.layout.addWidget(self.filter_label)
        self.layout.addWidget(self.filter_combo)
        self.layout.addWidget(self.slider_label)
        self.layout.addWidget(self.filter_slider)
        self.layout.addWidget(self.resize_label)
        self.layout.addWidget(self.resize_slider)
        self.layout.setContentsMargins(20, 20, 20, 20)

        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addStretch()
        central_layout.addLayout(self.layout)
        central_layout.addStretch()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        self.original_image = None
        self.loaded_image = None
        self.filtered_image = None

    def load_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.original_image = cv2.imread(file_path)
            self.loaded_image = self.original_image.copy()  # Make a copy for processing
            self.display_image(self.loaded_image)
            self.display_image_size(self.original_image)  # Display original image size

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

    def display_image_size(self, image):
        if image is None:
            return
        h, w, _ = image.shape
        self.size_label.setText(f"Original Image Size: {w}x{h}")

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

    def resize_image(self):
        if self.original_image is None:
            return
        scale_percent = self.resize_slider.value() / 100
        width = int(self.original_image.shape[1] * scale_percent)
        height = int(self.original_image.shape[0] * scale_percent)
        resized_image = cv2.resize(self.original_image, (width, height), interpolation=cv2.INTER_AREA)
        self.loaded_image = resized_image
        self.apply_filter()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFilteringApp()
    window.show()
    sys.exit(app.exec_())
