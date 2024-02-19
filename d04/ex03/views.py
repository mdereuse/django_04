from django.shortcuts import render

def index(request):
    black_color_range =  [
        f"#{i:02X}{i:02X}{i:02X}" for i in range(5, 255, 5)
    ]
    red_color_range =  [
        f"#{i:02X}0000" for i in range(5, 255, 5)
    ]
    blue_color_range =  [
        f"#0000{i:02X}" for i in range(5, 255, 5)
    ]
    green_color_range =  [
        f"#00{i:02X}00" for i in range(5, 255, 5)
    ]
    context = {
        "color_range": zip(black_color_range, red_color_range, blue_color_range, green_color_range)
    }
    return render(request, 'ex03/index.html', context)
