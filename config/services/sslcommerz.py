from config.env import BASE_DIR, env
import os
from datetime import timedelta



# SSLCommerz settings
SSLCOMMERZ_STORE_ID = env('SSLCOMMERZ_STORE_ID', default='')
SSLCOMMERZ_STORE_PASSWORD = env('SSLCOMMERZ_STORE_PASSWORD', default='')
SSLCOMMERZ_API_URL = env('SSLCOMMERZ_API_URL', default='https://sandbox.sslcommerz.com/gwprocess/v4/api.php')
SSLCOMMERZ_VALIDATION_URL = env('SSLCOMMERZ_VALIDATION_URL', default='https://sandbox.sslcommerz.com/validator/api/validationserverAPI.php')
SSLCOMMERZ_SANDBOX_MODE = env('SSLCOMMERZ_SANDBOX_MODE', default=True)

