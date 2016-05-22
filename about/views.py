from django.shortcuts import render_to_response


from common.generator import Generator

def about(request):
    #puzzle = Generator(9, 9).generate()
    puzzle = [
        [0, 7, 8, 5, 6, 0, 1, 0, 0],
        [0, 2, 3, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 0, 0, 2, 6, 0, 0],
        [7, 0, 0, 0, 9, 1, 0, 5, 3],
        [0, 8, 0, 0, 4, 0, 0, 6, 0],
        [4, 3, 0, 6, 2, 0, 0, 0, 1],
        [0, 0, 6, 2, 0, 0, 0, 0, 0],
        [0, 4, 7, 0, 0, 0, 3, 8, 0],
        [0, 0, 1, 0, 3, 6, 7, 2, 0]
    ]

    context = {'puzzle': puzzle}

    print context
    return render_to_response('about/contact.html', context)


def contact(request):
    #puzzle = Generator(9, 9).generate()
    puzzle = [
        [0, 7, 8, 5, 6, 0, 1, 0, 0],
        [0, 2, 3, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 0, 0, 2, 6, 0, 0],
        [7, 0, 0, 0, 9, 1, 0, 5, 3],
        [0, 8, 0, 0, 4, 0, 0, 6, 0],
        [4, 3, 0, 6, 2, 0, 0, 0, 1],
        [0, 0, 6, 2, 0, 0, 0, 0, 0],
        [0, 4, 7, 0, 0, 0, 3, 8, 0],
        [0, 0, 1, 0, 3, 6, 7, 2, 0]
    ]

    context = {'puzzle': puzzle}

    print context
    return render_to_response('about/about.html', context)
