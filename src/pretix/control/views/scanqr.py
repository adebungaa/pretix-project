from django.shortcuts import render

def scan_qr(request):
    # Anda bisa meneruskan data ke template jika diperlukan
    return render(request, 'scan_qr.html')
