from util import score_slideshows


def num_edge_tags(slideshow):
    num_tags = len(slideshow.slides[0].tags)
    if len(slideshow.slides) > 1:
        num_tags += len(slideshow.slides[-1].tags)
    return num_tags


def find_match(slideshow, slideshows):

    best_score = 0
    best_idx = 0
    for idx, ss in enumerate(slideshows):
        score = score_slideshows(slideshow, ss)
        if score >= best_score:
            best_score = score
            best_idx = idx
        if idx >= 1000:
            break

    # print('best score:', best_score, 'idx:', best_idx)
    return best_idx


def combine_slideshows(slideshows):

    sorted_slideshows = slideshows
    sorted_slideshows = sorted(sorted_slideshows, key=lambda s: num_edge_tags(s), reverse=True)
    while len(sorted_slideshows) > 1:
        slideshow = sorted_slideshows.pop()
        idx = find_match(slideshow, sorted_slideshows)
        sorted_slideshows[idx].add_slideshow(slideshow)
        # print(slideshow.slides[0].tags)
        # print(slideshow.slides[-1].tags)
        # print('left to do:', len(sorted_slideshows))

    return sorted_slideshows[0]





