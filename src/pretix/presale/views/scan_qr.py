from django.shortcuts import render

def scan_qr(request):
    return render(request, 'templates/pretixpresale/event/scan_qr.html')  # Template untuk scanner
