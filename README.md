
# 🌐 Kerem Sert - Personal Portfolio Website

Bu proje, tam kapsamlı web geliştirme becerilerimi uyguladığım bireysel portföy sitemdir.  
Backend kısmı Django ile, frontend ise JavaScript, HTML ve CSS kullanılarak oluşturulmuş; proje Docker ile container haline getirilmiştir.

## 🚀 Özellikler

- 🧠 Django tabanlı backend mimarisi  
- 🎨 HTML/CSS ile modern ve sade kullanıcı arayüzü  
- 📦 Docker ile containerize edilmiş yapı  
- 📄 Proje tabanlı içerik sunumu ve tanıtım bölümleri  

## ⚙️ Kullanılan Teknolojiler

- Python  
- JavaScript
- Django
- PostgreSQL 
- Docker  
- HTML5 / CSS3

## 🧪 Kurulum ve Çalıştırma

1. **Repozitoyu Klonla**
```bash
git clone https://github.com/keremsert54/keremsert-website.git
cd keremsert-website
```

2. **Docker ile Çalıştır**
```bash
docker build -t keremsert-website .
docker run -p 8000:8000 keremsert-website
```

3. **Tarayıcıdan Aç**  
[http://localhost:8000](http://localhost:8000) adresinden uygulamaya erişebilirsiniz.

> Not: Docker yüklü değilse, [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) adresinden kurulum yapabilirsiniz.

## 📁 Proje Yapısı

```
keremsert-website/
├── app/                   # Django uygulama dizini  
│   ├── templates/         # HTML dosyaları  
│   ├── static/            # CSS ve medya dosyaları  
│   ├── views.py           # Görünümler  
│   └── models.py          # Veritabanı modelleri  
├── Dockerfile             # Docker yapılandırma dosyası  
├── requirements.txt       # Proje bağımlılıkları  
└── manage.py              # Django yönetim komutu
```

## 👤 Geliştirici

**Kerem Sert**  
2.sınıf Bilişim Sistemleri Mühendisliği öğrencisi

- 📌 [LinkedIn](https://www.linkedin.com/in/keremsert/)  
- 💻 [GitHub](https://github.com/keremsert54)

## 📄 Lisans

MIT Lisansı © 2025 Kerem Sert

---

Bu dosya keremsert-website projesini açık ve profesyonel şekilde tanıtmak için hazırlanmıştır.
