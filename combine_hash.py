from util import score_slideshows, SlideShow, Slide
from collections import defaultdict

def combine_hash(slideshows):

    slides = [slideshow.slides[0] for slideshow in slideshows]

    tag_hash = defaultdict(list)
    for id_, slide in enumerate(slides):
        for tag in slide.tags:
            tag_hash[tag].append(id_)

    remaining_slides = len(slides)

    current_slide = slides[0]
    slides[0] = None
    remaining_slides -= 1

    slideshow = SlideShow(current_slide)

    while remaining_slides > 0:
        possible_slides = set()
        for tag in current_slide.tags:
            ids = tag_hash[tag]
            possible_slides |= set(ids)

        for possible_slide in possible_slides:
            if slides[possible_slide] is not None:
                current_slide = slides[possible_slide]
                slides[possible_slide] = None
                remaining_slides -= 1

                slideshow.add_slideshow(SlideShow(current_slide))
                break
        else:
            possible_slide, current_slide = next((id_, slide_) for id_, slide_ in enumerate(slides) if slide_ is not None)
            slides[possible_slide] = None
            remaining_slides -= 1


    return slideshow
