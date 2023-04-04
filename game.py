import openai_secret_manager
import openai
import time

# OpenAI API anahtarlarını almak için kullanılan fonksiyon
def get_openai_secrets():
    return openai_secret_manager.get_secret("openai")

secrets = get_openai_secrets()
openai.api_key = secrets["api_key"]


def generate_response(prompt):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100,
      n=1,
      stop=None,
      frequency_penalty=0,
      presence_penalty=0
    )

    message = response.choices[0].text.strip()
    return message

def play_game():
    # Karakter özellikleri
    player = {
        "name": "",
        "health": 100,
        "damage": 50,
        "defense": 30,
        "experience": 0
    }

    # Zindandaki odaların listesi
    dungeon = [
        {"name": "Goblin Odası", "description": "Karanlık bir oda, ortasında bir goblin var."},
        {"name": "Zırh Odası", "description": "Duvarlar zırhlarla kaplı bir oda."},
        {"name": "Hazineler Odası", "description": "Odada büyük bir sandık var, içinde hazineler olabilir."}
    ]

    # Oyunun başlangıcı
    print("Hoşgeldiniz! Lütfen bir karakter adı girin.")
    player["name"] = input("Adınız: ")

    print("Merhaba, {}. Maceranız başlıyor.".format(player["name"]))

    # Zindan keşfi başlıyor
    for room in dungeon:
        print("Girilen oda: ", room["name"])
        print(room["description"])

        # GPT-3 kullanarak yapay zeka yanıtı oluşturun
        prompt = "Odanın ortasındaki yaratıkla savaşmak mı istersin? Hayır/Evet"
        response = generate_response(prompt)

        # Yapay zeka yanıtına göre oyun ilerletin
        if "Hayır" in response:
            print("Yaratıkla savaşmadan odadan ayrıldınız.")
        else:
            print("Yaratıkla savaşmaya karar verdiniz!")
            enemy = {"name": "Goblin", "health": 50, "damage": 20, "defense": 10}

            while enemy["health"] > 0 and player["health"] > 0:
                # Oyuncunun saldırısı
                enemy["health"] -= player["damage"] - enemy["defense"]
                print("Yaratığa {} hasar verildi, kalan canı: {}".format(player["damage"] - enemy["defense"], enemy["health"]))

                # Yaratığın saldırısı
                player["health"] -= enemy["damage"]
                print("Sana {} hasar verdi, kalan canın: {}".format(enemy["damage"], player["health"]))

            if enemy["health"] <= 0:
                print("Yaratığı yendiniz! +10 deneyim kazandınız.")
                player["experience"] += 10

            if player["health"] <= 0:
                print("Üzgünüm, {}. Hayatını kaybettin. Oyun bitti.".format(player["name"]))
                return
            else:
                print("Tebrikler, yaratığı yendiniz!")
                player["experience"] += 50
                print("50 deneyim kazandınız, toplam deneyim: {}".format(player["experience"]))

        # Hazineler odası
        if room["name"] == "Hazineler Odası":
            print("Odada bir sandık var.")
            prompt = "Sandığı açmak istiyor musunuz? Hayır/Evet"
            response = generate_response(prompt)

            if "Hayır" in response:
                print("Sandığı açmadan odadan ayrıldınız.")
            else:
                print("Sandığı açmaya karar verdiniz!")
                treasure = {"gold": 100, "gem": "Safir"}
                print("Sandıktan {} adet altın ve {} taş çıktı.".format(treasure["gold"], treasure["gem"]))
                player["experience"] += 20
                print("20 deneyim kazandınız, toplam deneyim: {}".format(player["experience"]))

    print("Tebrikler, {}! Tüm odaları keşfettiniz. Oyunu tamamladınız.".format(player["name"]))

play_game()
