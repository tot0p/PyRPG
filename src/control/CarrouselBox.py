from kivy.uix.carousel import Carousel

class CarrouselBox(Carousel):
    '''
    carousel kivy modifié pour disable le scrolling via la souris
    '''

    def on_touch_down(self, touch):
        return None

    def on_touch_move(self, touch):
        return None

    def on_touch_up(self, touch):
        return None
