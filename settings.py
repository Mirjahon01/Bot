db_url='sqlite:///db.sqlite'

ref_pay_perc_1lvl=0.09  #столько получит от 1 уровная рефералов за оплату
ref_pay_perc_2lvl=0.03  #столько получит от 2 уровная рефералов за оплату
ref_view_pay_1lvl=0.15  #столько получит от 1 уровная рефералов за подписку
ref_view_pay_2lvl=0.05  #столько получит от 2 уровная рефералов за подписку
new_ref_cost=0.2       #автоначисление за нового реферала.в копейках.
user_view_perc=0.50  #столько получит пользователь за вступление(проценты от стоимости установленной заказчиком)
min_out_pay=20  #минимальная сумма для вывода
min_post_cost=0.4  #минимальная стоимость 1 подписчика
user_post_perc=0.50 #процент от цены просмотра  
user_timewait_sec=6  #время просмотра поста
min_view_cost=0.04   #минимальная стоимость 1 просмотра


number=""
qiwi_token =''

ya_number=''
ya_token='00'
telegram_token=''



uah_to_rub=2.42
usd_to_rub=65.85
eur_to_rub=75.73

admins = [366584392]
bans = []

tutorial_url = 'https://teletype.in/@seryoga205/ByjHaPBXQ'





WEBHOOK_HOST = '194.87.109.3'
WEBHOOK_PORT = 88
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_CERT = './webhook_cert.pem'
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'



WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)

WEBHOOK_URL_PATH = "/{}/".format(telegram_token)