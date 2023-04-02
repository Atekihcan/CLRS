import json
from PIL import Image, ImageDraw, ImageFont

W = 1200
H = 630

# Open fonts
times_120 = ImageFont.truetype('/mnt/c/Windows/Fonts/times.ttf', 120)
arial_black_40 = ImageFont.truetype('/mnt/c/Windows/Fonts/ariblk.ttf', 40)
arial_black_52 = ImageFont.truetype('/mnt/c/Windows/Fonts/ariblk.ttf', 52)

# Open TOC JSON
toc_data = None
with open('_data/toc.json') as f:
    toc_data = json.load(f)

def CreateImageDirect(title, problem_title, location):
    # Create Image
    img = Image.new('RGB', (W, H), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Write texts
    d.rectangle([W/2 - 260, 50, W/2 + 260, 120], fill = (71, 41, 163))
    d.text((W/2, 100), "CLRS SOLUTIONS", font=arial_black_40, fill = (255, 255, 255), anchor="ms")
    d.text((W/2, 180), problem_title, font=arial_black_52, fill = (45, 25, 120), anchor="ms")
    d.rectangle([W/2 - 260, 120, W/2 + 260, 200], outline = (71, 41, 163), width=4)
    d.text((W/2, 360), title, font=times_120, fill = (0, 0, 0), align="center", anchor="ms", spacing=20)

    # Save image
    img.save(location)

def CreateImage(chapter, section, problem_id):
    title = ''
    problem_title = ''
    image_folder = ''
    image_filename = ''

    if isinstance(chapter, int):
        image_folder = f"assets/img/{chapter:02d}/"
    else:
        image_folder = f"assets/img/{chapter}/"

    if section > 0:
        problem_title = f"Exercise {chapter}.{section}-{problem_id}"
        image_filename = f"{chapter}.{section:}-{problem_id}.jpg"
        if isinstance(chapter, int):
            title = toc_data['chapters'][chapter - 1]['sections'][int(section) - 1]['name']
        else:
            title = toc_data['appendices'][int(chapter) - 'A']['sections'][int(section) - 1]['name']
    else:
        problem_title = f"Problem {chapter}-{problem_id}"
        image_filename = f"{chapter}-{problem_id}.jpg"
        if isinstance(chapter, int):
            title = toc_data['chapters'][chapter - 1]['problems'][problem_id - 1]['name']
        else:
            title = toc_data['appendices'][int(chapter) - 'A']['problems'][problem_id - 1]['name']
    
    title_parts = title.split(' ')
    title = ''
    num_chars = 0
    for part in title_parts:
        title += part + ' '
        num_chars += len(part)
        if (num_chars > 12):
            num_chars = 0
            title += '\n'

    # Create Image
    img = Image.new('RGB', (W, H), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Write texts
    d.rectangle([W/2 - 260, 50, W/2 + 260, 120], fill = (71, 41, 163))
    d.text((W/2, 100), "CLRS SOLUTIONS", font=arial_black_40, fill = (255, 255, 255), anchor="ms")
    d.text((W/2, 180), problem_title, font=arial_black_52, fill = (45, 25, 120), anchor="ms")
    d.rectangle([W/2 - 260, 120, W/2 + 260, 200], outline = (71, 41, 163), width=4)
    d.text((W/2, 360), title, font=times_120, fill = (0, 0, 0), align="center", anchor="ms", spacing=20)

    # Save image
    img.save(image_folder + image_filename)

# chapter = 1
# prob_list = [
#     [i for i in range(1, 2)],
#     [i for i in range(1, 6)],
#     [i for i in range(1, 4)]
# ]

# chapter = 2
# prob_list = [
#     [i for i in range(1, 5)],
#     [i for i in range(1, 5)],
#     [i for i in range(1, 5)],
#     [i for i in range(1, 7)]
# ]

# chapter = 3
# prob_list = [
#     [i for i in range(1, 7)],
#     [i for i in range(1, 9)],
#     [i for i in range(1, 9)]
# ]

# chapter = 4
# prob_list = [
#     [i for i in range(1, 1)],
#     [i for i in range(1, 6)],
#     [i for i in range(1, 8)],
#     [i for i in range(1, 10)],
#     [i for i in range(1, 8)],
#     [i for i in range(1, 5)]
# ]

# for section, lst in enumerate(prob_list):
#     if section == 0:
#         continue
#     for prob in lst:
#         CreateImage(chapter, section, prob)

for i in range(1, 8):
    CreateImageDirect("Recursion-tree Method\nfor Solving Recurrences", f"Exercise 4.4-{i}", f"assets/img/04/4.4-{i}.jpg")