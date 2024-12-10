from django.shortcuts import render
from django.http import JsonResponse
import requests

def validation_ticket(request):
    if request.method == "POST":
        # Ambil data dari request POST (hasil scan tiket)
        ticket_code = request.POST.get('ticket_code')
        action = request.POST.get('action')  # Masuk/Keluar

        try:
            # Contoh panggil API untuk validasi tiket
            response = requests.post(
                'http://api.pretix.local/validate-ticket/',
                data={'ticket_code': ticket_code, 'action': action}
            )
            data = response.json()

            # Simpan hasil validasi ke database atau tampilkan pesan
            if data['status'] == 'success':
                return JsonResponse({'message': 'Validasi berhasil'})
            else:
                return JsonResponse({'message': 'Validasi gagal'})
        except Exception as e:
            return JsonResponse({'message': 'Error saat memvalidasi tiket', 'error': str(e)})

    # Render halaman validasi tiket untuk GET request
    return render(request, 'pretixcontrol/validasi_tiket.html')
