## NOT ##
# Parantez içindeki yazılar açıklamadır yazılmayacaktır #

mkdir projeAdı -> Proje dizini oluştur

python3 -m venv env (env sanal sunucu ismi) -> Sanal bir python sunucusu oluştur

source env/bin/activate -> Sanal sunucuyu aktif et (deactivate ile durdurulabilir)

pip install django==1.11.7 -> Django 1.11.7 yükle

django-admin startproject election . (election proje ismi) -> Django projesi oluştur

urls.py dosyasına eklenen views için views.py dosyası oluştur

python manage.py runserver -> Uygulamayı başlatan komut

python manage.py makemigrations election (election uygulama ismi)
python manage.py makemigrations profile (profile uygulama ismi)
python manage.py migrate

python manage.py createsuperuser -> Kullanıcı oluşturmak için verilen komut

http://localhost:8000/admin/ -> Yönetim paneli url'i

Oluşturduğunuz kullanıcı ile giriş yapabilirsiniz

touch requirements.txt -> requirements adında bir dosya oluşturur

pip freeze -> kurulu modülleri listeler

requirements.txt içine pip freeze çıktıları kopyalanır

pip install -r requirements.txt -> venv (sanal sunucu) silinmesi durumunda requirements.txt dosyasındaki modülleri kurar

pip install django-import-export -> django-import-export modülünü kurar

## Semantik Versiyonlama ##
Majör değişiklik (1.0.0) database, dil, vs.
Minör değişiklik (1.1.0) yeni özellik, arayüz vs.
Bug fix, build (1.1.1) yama, hata düzeltmeleri vs.
Bir kısı sürüm atlarsa sağ taraf sıfırlanır

## Git ##

git config --global user.name "isim"
git config --global user.email "email"
git init .
git add --all
git remote add origin <repo url>
git commit -m "mesaj"
git push origin master
