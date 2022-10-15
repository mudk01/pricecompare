import requests
#from bs4 import BeautifulSoup

amazon_product_url = "https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863TXGM3"
#target_product_url = "https://www.target.com/p/sony-wh-1000xm4-noise-canceling-overhead-bluetooth-wireless-headphones-black/-/A-79757327?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&DFA=71700000014846099&CPNG=PLA_Electronics%2BShopping_Brand%7CElectronics_Ecomm_Hardlines&adgroup=SC_Electronics&LID=700000001170770pgs&LNM=PRODUCT_GROUP&network=g&device=c&location=9032493&targetid=pla-82462042369&ds_rl=1246978&ds_rl=1248099&gclid=CjwKCAjwtKmaBhBMEiwAyINuwKgPr2kaaazHNLcM_RJiMmb3TyeqlyoMI1BZQTGkbNPIxUmHq_GTdxoCDd0QAvD_BwE&gclsrc=aw.ds"
#walmart_product_url = "https://www.walmart.com/ip/Sony-WH-1000XM4-Wireless-Noise-Canceling-Over-the-Ear-Headphones-with-Google-Assistant-Black/310157752?wmlspartner=wlpa&selectedSellerId=0&wl13=2697&adid=22222222277310157752_117755028669_12420145346&wmlspartner=wmtlabs&wl0=&wl1=g&wl2=c&wl3=501107745824&wl4=pla-294505072980&wl5=9032493&wl6=&wl7=&wl8=&wl9=pla&wl10=8175035&wl11=local&wl12=310157752&wl13=2697&veh=sem_LIA&gclid=CjwKCAjwtKmaBhBMEiwAyINuwL_2qY0OX-8lRl1avU2qYn_QDkjO6liA0-8_HnPEaAua1aNI6Km0yBoC7uAQAvD_BwE&gclsrc=aw.ds"

page = requests.get(amazon_product_url)

print(page.text)

#soup = BeautifulSoup(page.content, "html=parser")