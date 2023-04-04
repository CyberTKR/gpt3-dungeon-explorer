GPT-3 Dungeon Explorer

GPT-3 Dungeon Explorer, OpenAI'nin GPT-3 yapay zekası kullanılarak oluşturulmuş basit bir metin tabanlı oyun simülasyonudur. Oyuncular, karakterlerini yöneterek bir zindan keşfederler ve farklı odalardaki yaratıklarla savaşır veya hazine arayışına girerler.

Kurulum

Bu repo'yu bilgisayarınıza kopyalayın: git clone https://github.com/CyberTKR/gpt3-dungeon-explorer.git


## Requirements

- Python 3.x
- `openai`
Gerekli kütüphaneleri yükleyin: `pip3 install openai`
game.py dosyasını çalıştırın: `python3 game.py`

Oynanış

Oyun, oyunculara karakter adı sorarak başlar ve ardından zindandaki odaların listesi gösterilir. Her odaya girdiklerinde, oyunculara yapay zeka tarafından üretilen bir yanıt sunulur ve oyuncuların karar vermesi gerekir.

Yaratıklarla savaşmak isteyen oyuncular, düşmanın sağlık ve saldırı gücünü dikkate alarak stratejilerini belirlemelidirler. Hazine odaları, oyunculara karakter özellikleri için ödüller veren hazineler içerebilir.

Oyuncular, karakterlerinin can puanları sıfırlanmadan önce mümkün olduğunca çok düşman yenmeye çalışmalıdırlar. Ayrıca, yaptıkları her savaş ve her oda keşfi için deneyim kazanırlar.

Lisans

Bu proje GNU General Public License v3.0 lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakınız.


GPT-3 Dungeon Explorer

GPT-3 Dungeon Explorer is a simple text-based game simulation created using OpenAI's GPT-3 artificial intelligence. Players explore a dungeon and battle creatures or search for treasure by managing their characters.

Installation

Clone this repo to your computer: git clone https://github.com/CyberTKR/gpt3-dungeon-explorer.git
Install the required libraries:  `pip3 install openai`
Run the game.py file: `python3 game.py`
Gameplay

The game starts by asking players for a character name, and then shows a list of rooms in the dungeon. Every time they enter a room, players are presented with an AI-generated response and must make decisions.

Players who want to fight creatures must determine their strategies based on the enemy's health and attack power. Treasure rooms may contain rewards for players' character attributes.

Players must try to defeat as many enemies as possible before their characters' health points are depleted. They also gain experience for each battle and each room exploration.

License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
