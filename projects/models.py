from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from colorthief import ColorThief

TECHNOLOGIES = [
    ('Misc', 'Misc'),
    ('Chicken', 'Chicken'),
    ('Beef', 'Beef'),
    ('Pork', 'Pork'),
    ('Seafood', 'Seafood'),
    ('Vegetable', 'Vegetable'),
]

RATING_SCALE = [(i, i) for i in range(1,11)]
HEAT_SCALE = [(i, i) for i in range(1,6)]

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    technology = models.CharField(max_length=20, choices=TECHNOLOGIES, default='Misc')
    heat = models.DecimalField(max_digits=1, decimal_places=0, choices=HEAT_SCALE, default=1)
    rating = models.DecimalField(max_digits=2, decimal_places=0, choices=RATING_SCALE, default=1)
    image = ProcessedImageField(upload_to='img',
                                            processors=[ResizeToFill(400, 400)],
                                            format='JPEG',
                                            options={'quality': 60})
    #color1 = models.CharField(max_length=100, default="100,100,100")
    #color2 = models.CharField(max_length=100, default="100,100,100")
    #color3 = models.CharField(max_length=100, default="100,100,100")

    # create list of the dominant 3 colors in image, using k=6 clusters
    # used to make themed titles for each ramen detail page
    def getColors(self):
        color_thief = ColorThief(self.image.path)
        dominant_colors = color_thief.get_palette(6,20)

        # strip off the opening and closing parens from get_palette output
        # return a list of the 3 most dominant colors
        return [str(dominant_colors[i])[1:-1] for i in range(3)]
        #colorList =  [str(dominant_colors[i])[1:-1] for i in range(3)]
        #self.color1 = colorList[0]
        #self.color1 = colorList[1]
        #self.color1 = colorList[2]
    def __str__(self):
        return self.title
