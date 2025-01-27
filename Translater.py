from deep_translator import GoogleTranslator


def translate_text(text, source_lang, target_lang):
    try:
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated_text
    except Exception as e:
        print(f"Çeviri sırasında bir hata oluştu: {e}")
        return None


def list_supported_languages():
    try:
        translator = GoogleTranslator()
        languages = translator.get_supported_languages()
        print("Desteklenen Diller:")
        for lang in languages:
            print(f"- {lang}")
    except Exception as e:
        print(f"Dilleri listelerken bir hata oluştu: {e}")


def main():
    print("--- Çeviri Uygulaması ---")
    while True:
        print("\nSeçenekler:")
        print("1. Metin Çevir")
        print("2. Desteklenen Dilleri Listele")
        print("3. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            text = input("Çevrilecek metni girin: ")
            source_lang = input("Çevirmek istediğiniz metin dilini giriniz. (ör. 'en' İngilizce, 'tr' Türkçe): ")
            target_lang = input("Hangi dile çevirmek istiyorsunuz?(ör. 'en' İngilizce, 'tr' Türkçe): ")
            translated_text = translate_text(text, source_lang, target_lang)
            if translated_text:
                print(f"Çeviri: {translated_text}")

        elif choice == "2":
            list_supported_languages()

        elif choice == "3":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
