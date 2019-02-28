from util import Slide, SlideShow


def algorithm(photo_collection):
    s1 = SlideShow(Slide(photo_collection.photos[0]))
    s2 = SlideShow(Slide(photo1=photo_collection.photos[1],
                         photo2=photo_collection.photos[2]))
    s3 = SlideShow(Slide(photo_collection.photos[3]))

    return [s1, s2, s3]
