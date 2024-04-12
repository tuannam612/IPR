from PIL import Image, ImageEnhance,ImageFilter
import os;
def convert_to_grey(image_path, output_path):
    img = Image.open(image_path)
    grey_scale = img.convert("L")
    grey_scale.save(output_path)
    
convert_to_grey("public/flower.jpg", "public/flower_Grey.jpg")
    

def resize_image(image_path, output_path, new_size):
    img = Image.open(image_path)
    resized_img = img.resize(new_size)
    resized_img.save(output_path)

resize_image("public/flower.jpg", "public/flower_resize.jpg",(50,50))

def crop_image(image_path, output_path, crop_box):
    img = Image.open(image_path)
    crop_img = img.crop(crop_box)
    crop_img.save(output_path)
    
crop_image("public/flower.jpg", "public/flower_crop.jpg", (50, 50, 250, 150))


def enhanced_img(image_path, output_path):
    img = Image.open(image_path)
    contrast_factor = 1.5
    contrast = ImageEnhance.Contrast(img)
    image_with_contrast = contrast.enhance(contrast_factor)
    brightness_factor = 1.2  
    brightness = ImageEnhance.Brightness(image_with_contrast)
    image_with_brightness = brightness.enhance(brightness_factor)
    image_with_brightness.save(output_path)
enhanced_img("public/flower.jpg", "public/flower_enh.jpg")

def rotate_and_flip_image(image_path, output_path):
    original_image = Image.open(image_path)
    rotated_image_90 = original_image.rotate(90)
    rotated_image_180 = original_image.rotate(180)
    flipped_horizontal_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_vertical_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)
    rotated_image_90.save(f'{output_path}/rotated_image_90.jpg')
    rotated_image_180.save(f'{output_path}/rotated_image_180.jpg')
    flipped_horizontal_image.save(f'{output_path}/flipped_horizontal_image.jpg')
    flipped_vertical_image.save(f'{output_path}/flipped_vertical_image.jpg')

rotate_and_flip_image("public/flower.jpg", "public")


def apply_filters(image_path, output_path):
    original_image = Image.open(image_path)
    blurred_image = original_image.filter(ImageFilter.BLUR)
    sharpened_image = original_image.filter(ImageFilter.SHARPEN)
    blurred_image.save(f'{output_path}/blurred_image.jpg')
    sharpened_image.save(f'{output_path}/sharpened_image.jpg')
apply_filters("public/flower.jpg", "public")
