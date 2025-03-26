from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def parse_reviews(text):
    try:
        text = text.strip().replace(',', '')
        if 'K' in text:
            return int(float(text.replace('K', '')) * 1000)
        elif 'M' in text:
            return int(float(text.replace('M', '')) * 1000000)
        return int(text) if text.isdigit() else 0  # Retorna 0 se não for número válido
    except ValueError:
        return 0  # Evita falha na conversão

# Lista de URLs para acessar
regions = [
    "https://www.xbox.com/pt-BR/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Brasil
    "https://www.xbox.com/en-us/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # EUA
    "https://www.xbox.com/en-gb/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Reino Unido
    "https://www.xbox.com/en-ca/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Canadá
    "https://www.xbox.com/en-au/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Austrália
    "https://www.xbox.com/fr-fr/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # França
    "https://www.xbox.com/de-de/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Alemanha
    "https://www.xbox.com/es-mx/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # México
    "https://www.xbox.com/it-it/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Itália
    "https://www.xbox.com/es-es/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Espanha
    "https://www.xbox.com/nl-nl/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Países Baixos
    "https://www.xbox.com/sv-se/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Suécia
    "https://www.xbox.com/no-no/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Noruega
    "https://www.xbox.com/da-dk/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Dinamarca
    "https://www.xbox.com/fi-fi/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Finlândia
    "https://www.xbox.com/ru-ru/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Rússia
    "https://www.xbox.com/pt-pt/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Portugal
    "https://www.xbox.com/ja-jp/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Japão
    "https://www.xbox.com/ko-kr/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Coreia do Sul
    "https://www.xbox.com/tr-tr/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Turquia
    "https://www.xbox.com/ar-sa/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Arábia Saudita
    "https://www.xbox.com/pt-za/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # África do Sul
    "https://www.xbox.com/es-ar/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Argentina
    "https://www.xbox.com/fr-be/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Bélgica (Francês)
    "https://www.xbox.com/es-co/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Colômbia
    "https://www.xbox.com/el-gr/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Grécia
    "https://www.xbox.com/sk-sk/games/store/grand-theft-auto-v-xbox-one/bpj686w6s0nh",  # Eslováquia
]

driver = webdriver.Chrome()
total_reviews = 0

for region in regions:
    driver.get(region)
    
    try:
        # Espera até o elemento estar presente (máx. 10 segundos)
        reviews_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Rating-module__totalRatings___i594Q"))
        )
        
        reviews_text = reviews_element.text.strip()
        if reviews_text:
            region_reviews = parse_reviews(reviews_text)
            total_reviews += region_reviews
            print(f"{region}: {region_reviews} avaliações")
        else:
            print(f"{region}: sem avaliações ou página do jogo")
    
    except Exception:
        print(f"{region}: sem avaliações ou página do jogo")

driver.quit()
print(f"\nTotal de avaliações: {total_reviews}")
