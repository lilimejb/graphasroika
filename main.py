from PIL import Image, ImageDraw, ImageFont
from random import randint


class GraphMaker:
    def __init__(self, matrix, width, height):
        self.matrix = [[bool(num) for num in elem] for elem in matrix]
        self.image = Image.new('RGB', (width, height))
        self.font = ImageFont.truetype("arial.ttf", 50)

    def builder(self, image):
        drawer = ImageDraw.Draw(image)
        points = [(randint(0, 860), randint(0, 860)) for i in range(len(self.matrix))]
        print(points)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    drawer.line((points[i], points[j]), width=5, fill=128)
                    drawer.text((points[i][0] - 10, points[i][1] - 10), str(i + 1), font=self.font)


    def make_image(self):
        self.builder(self.image)
        self.image.save('test.png')


maker = GraphMaker([[0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 0], [1, 0, 1, 0]], 1080, 980)
maker.make_image()
print(maker.matrix)