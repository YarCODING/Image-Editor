from PIL import Image, ImageFilter, ImageEnhance

class ImageEditor():
    def __init__(self):
        self.directory = None
        self.original = None
        self.edited = None
        self.editedphotos = []

    def open(self, directory:str):
        self.directory = directory
        self.original = Image.open(f'{self.directory}')
        self.edited = self.original

    def close(self):
        self.directory = None
        self.original = None


    def show_original(self):
        self.original.show()
    
    def show_edited(self):
        self.edited.show()


    def do_mirror(self):
        self.edited = self.edited.transpose(Image.FLIP_LEFT_RIGHT)
    
    def do_gray(self):
        self.edited = self.original.convert('L')

    def do_turn_90(self):
        self.edited = self.edited.transpose(Image.ROTATE_90)
    
    def do_turn_180(self):
        self.edited = self.edited.transpose(Image.ROTATE_180)

    def do_blur(self):
        self.edited = self.edited.filter(ImageFilter.BLUR)

    def do_crop(self, coordinates:tuple):
        self.edited = self.edited.crop(coordinates)

    def save(self, name):
        self.edited.save(name)

        self.editedphotos.append(self.edited)


editor = ImageEditor()