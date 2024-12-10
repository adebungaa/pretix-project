# ------------------------- SUKSES PANGGIL MIDTRANS
# from django.http import JsonResponse
# from midtransclient import Snap
# import os
# import time  # Tambahkan ini jika menggunakan timestamp untuk order_id
# import uuid  # Tambahkan ini jika menggunakan UUID untuk order_id
# from django.views.decorators.csrf import csrf_exempt

# MIDTRANS_SERVER_KEY = os.getenv("MIDTRANS_SERVER_KEY", "SB-Mid-server-cFPLXJf62ssnbSVqPcW0dUnI")
# MIDTRANS_CLIENT_KEY = os.getenv("MIDTRANS_CLIENT_KEY", "SB-Mid-client-TX3s1RgdsqHdHPbl")

# snap = Snap(
#     is_production=False,
#     server_key=MIDTRANS_SERVER_KEY
# )

# def create_payment(request):
#     transaction_details = {
#         "order_id": "order-id-python-" + str(request.user.id) + "-" + str(int(time.time())),  # Menggunakan timestamp untuk memastikan unique
#         "gross_amount": 100000,  # Jumlah dalam Rupiah
#     }
#     customer_details = {
#         "first_name": "Ade Bunga",
#         "last_name": "Dwi",
#         "email": "adebungads@gmail.com",
#         "phone": "083189241646",   
#     }
#     transaction_data = {
#         "transaction_details": transaction_details,
#         "customer_details": customer_details,
#     }

#     try:
#         transaction_token = snap.create_transaction(transaction_data)
#         return JsonResponse({
#             "status": "success",
#             "transaction_token": transaction_token['token']
#         })
#     except Exception as e:
#         return JsonResponse({
#             "status": "error",
#             "message": str(e)
#         }, status=500)

# ------------------------- SUKSES TARIK DATA 
import json
from django.http import JsonResponse
from midtransclient import Snap
import os
import time
import uuid 
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

MIDTRANS_SERVER_KEY = os.getenv("MIDTRANS_SERVER_KEY", "SB-Mid-server-cFPLXJf62ssnbSVqPcW0dUnI")
MIDTRANS_CLIENT_KEY = os.getenv("MIDTRANS_CLIENT_KEY", "SB-Mid-client-TX3s1RgdsqHdHPbl")

snap = Snap(
    is_production=False,
    server_key=MIDTRANS_SERVER_KEY
)
@csrf_exempt
@require_POST
def create_payment(request):
    try:
        # Debug log untuk cek request body
        print("Request body:", request.body)

        # Ambil data JSON dari permintaan POST
        data = json.loads(request.body)
        total_amount = data.get("totalAmount")

        # if total_amount is None:
        #     return JsonResponse({
        #         "status": "error",
        #         "message": "Total amount not provided"
        #     }, status=400)

        # Detail transaksi dengan total_amount yang dinamis
        transaction_details = {
            "order_id": "order-id-python-" + str(request.user.id) + "-" + str(int(time.time())),
            "gross_amount": total_amount  # Jumlah dalam Rupiah
        }
        
        customer_details = {
            "first_name": "Ade Bunga",
            "last_name": "Dwi",
            "email": "adebungads@gmail.com",
            "phone": "083189241646"
        }
        
        transaction_data = {
            "transaction_details": transaction_details,
            "customer_details": customer_details
        }

        # Buat transaksi dengan Midtrans
        transaction_token = snap.create_transaction(transaction_data)
        
        return JsonResponse({
            "status": "success",
            "transaction_token": transaction_token['token']
        })
    except Exception as e:
        # Log detail error untuk debugging
        print("Error in create_payment:", e)
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)
