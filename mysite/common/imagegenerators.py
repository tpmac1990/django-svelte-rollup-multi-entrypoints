from imagekit import ImageSpec, register
from imagekit.processors import Anchor, ResizeToFit, SmartResize

class GridImage(ImageSpec):
    processors = [
        SmartResize(height=200, width=200)
    ]
    format = 'WEBP'
    options = {'quality': 70}


register.generator('common:grid_image', GridImage)


class SlideImage(ImageSpec):
    processors = [
        ResizeToFit(height=350, width=250, anchor=Anchor.CENTER)
    ]
    format = 'WEBP'
    options = {'quality': 70}

register.generator('common:slide_image', SlideImage)