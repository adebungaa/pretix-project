import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def midtrans_webhook(request):
    if request.method == 'POST':
        try:
            # Ambil data JSON dari payload POST request
            payload = json.loads(request.body.decode('utf-8'))
            
            # Ambil data penting dari payload
            transaction_status = payload.get('transaction_status')
            order_id = payload.get('order_id')
            payment_type = payload.get('payment_type')
            fraud_status = payload.get('fraud_status')

            # Contoh logika: Update database berdasarkan status transaksi
            if transaction_status == 'capture':
                if payment_type == 'credit_card':
                    if fraud_status == 'accept':
                        # Update status pembayaran menjadi 'Success' di database
                        print(f"Transaction {order_id} successfully captured using {payment_type}.")
            elif transaction_status == 'settlement':
                # Update status pembayaran menjadi 'Settlement'
                print(f"Transaction {order_id} successfully settled.")
            elif transaction_status == 'pending':
                # Update status pembayaran menjadi 'Pending'
                print(f"Transaction {order_id} is pending.")
            elif transaction_status == 'deny':
                # Update status pembayaran menjadi 'Denied'
                print(f"Transaction {order_id} is denied.")
            elif transaction_status == 'expire':
                # Update status pembayaran menjadi 'Expired'
                print(f"Transaction {order_id} is expired.")
            elif transaction_status == 'cancel':
                # Update status pembayaran menjadi 'Cancelled'
                print(f"Transaction {order_id} is cancelled.")

            # Berikan respon sukses ke Midtrans
            return JsonResponse({'message': 'Webhook received successfully.'}, status=200)

        except json.JSONDecodeError:
            # Jika JSON tidak valid
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # Jika request bukan POST
    return JsonResponse({'error': 'Invalid request method'}, status=405)
