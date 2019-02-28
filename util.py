"""Utils."""


class SlideShow:

    def __init__(self, slide):
        self.slides = [slide]
        self.total_score = 0.0

    def add_slide(self, slideshow):
        score_left_left = score(self.slides[0], slideshow.slides[0])
        score_left_right = score(self.slides[0], slideshow.slides[-1])
        score_right_right = score(self.slides[-1], slideshow.slides[-1])
        score_right_left = score(self.slides[-1], slideshow.slides[0])

        top_score = max(score_left_left,
                        max(score_left_right,
                            max(score_right_right, score_right_left)))

        if score_left_left == top_score:
            self.slides = list(reversed(slideshow)) + self.slides
        elif score_left_right == top_score:
            self.slides = slideshow + self.slides
        elif score_right_left:
            self.slides += slideshow
        elif score_right_right:
            self.slides += list(reversed(slideshow))
        else:
            raise ValueError('Cant happen')
        self.total_score += top_score

    def __str__(self):
        output = ''
        for slide in self.slides:
            output += '{}\n'.format(str(slide))

        return output


class Slide:

    def __init__(self, photo1, photo2=None):
        self.ids = {photo1.id}
        self.tags = {*photo1.tags}

        if photo2 is not None:
            if photo1.orientation != 'V' and photo2.orientation != 'V':
                raise ValueError('2 photos in a slide needs to be vertical.')
            self.ids.union(photo2.id)
            self.tags.union(photo2.tags)
        elif photo1.orientation != 'H':
            raise ValueError('single photo slide need horizontal photo.')

    def __str__(self):
        """Output format"""
        return ' '.join([str(x) for x in self.ids])


def score(slide1, slide2):

    common_tags = len(slide1.tags.intersection(slide2.tags))
    diff1 = slide1.tags.difference(slide2.tags)
    diff2 = slide2.tags.difference(slide1.tags)

    return min(common_tags, min(diff1, diff2))
